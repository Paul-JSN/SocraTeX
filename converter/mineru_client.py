"""MinerU Precision API client for PDF-to-Markdown conversion."""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any

import requests

from converter.config import ConverterConfig


BASE_URL = "https://mineru.net/api/v4"

_POLL_INTERVAL_SECONDS = 3
_POLL_TIMEOUT_SECONDS = 600
_REQUEST_TIMEOUT_SECONDS = 30
_UPLOAD_TIMEOUT_SECONDS = 120


class MineruError(Exception):
    """Raised when a MinerU API call fails."""


class MineruAuthError(MineruError):
    """Raised on 401 — invalid or expired token."""


class MineruRateLimitError(MineruError):
    """Raised on 429 — too many requests."""


class MineruTaskError(MineruError):
    """Raised when a conversion task reports failure."""


# -- HTTP helpers ----------------------------------------------------------


def _auth_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def _check_response(resp: requests.Response) -> dict[str, Any]:
    if resp.status_code == 401:
        raise MineruAuthError(
            "Authentication failed (401). Check your MINERU_API_TOKEN."
        )
    if resp.status_code == 429:
        raise MineruRateLimitError(
            "Rate limit exceeded (429). Wait a moment and try again."
        )
    resp.raise_for_status()
    body: dict[str, Any] = resp.json()
    if body.get("code") not in (0, None):
        raise MineruError(f"API error: {body.get('msg', body)}")
    return body


# -- Pipeline steps --------------------------------------------------------


def _request_upload_urls(
    token: str,
) -> tuple[str, str, str]:
    """Request a batch_id and a pre-signed upload URL.

    Returns (batch_id, upload_url, object_name).
    """
    resp = requests.post(
        f"{BASE_URL}/file-urls/batch",
        headers=_auth_headers(token),
        json={"enable_formula": True},
        timeout=_REQUEST_TIMEOUT_SECONDS,
    )
    body = _check_response(resp)
    data = body["data"]
    batch_id: str = data["batch_id"]
    file_info = data["file_urls"][0]
    return batch_id, file_info["url"], file_info["object_name"]


def _upload_pdf(upload_url: str, pdf_path: Path) -> None:
    """Upload the PDF binary to the pre-signed URL."""
    pdf_bytes = pdf_path.read_bytes()
    resp = requests.put(
        upload_url,
        data=pdf_bytes,
        headers={"Content-Type": "application/octet-stream"},
        timeout=_UPLOAD_TIMEOUT_SECONDS,
    )
    resp.raise_for_status()


def _submit_task(
    token: str,
    batch_id: str,
    object_name: str,
    filename: str,
    model: str,
) -> str:
    """Submit an extraction task and return the task_id."""
    payload = {
        "batch_id": batch_id,
        "enable_formula": True,
        "language": "en",
        "model_version": model,
        "layout_model": "doclayout_yolo",
        "files": [
            {
                "name": filename,
                "is_ocr": False,
                "data_id": object_name,
            }
        ],
    }
    resp = requests.post(
        f"{BASE_URL}/extract/task",
        headers=_auth_headers(token),
        json=payload,
        timeout=_REQUEST_TIMEOUT_SECONDS,
    )
    body = _check_response(resp)
    task_id: str = body["data"]["task_id"]
    return task_id


def _poll_task(token: str, task_id: str) -> dict[str, Any]:
    """Poll until the task completes or fails.

    Returns the task data dict on success.
    """
    deadline = time.monotonic() + _POLL_TIMEOUT_SECONDS

    while time.monotonic() < deadline:
        resp = requests.get(
            f"{BASE_URL}/extract/task/{task_id}",
            headers=_auth_headers(token),
            timeout=_REQUEST_TIMEOUT_SECONDS,
        )
        body = _check_response(resp)
        state = body["data"].get("state", "")

        if state == "done":
            return body["data"]
        if state == "failed":
            raise MineruTaskError(
                f"Conversion task failed. Task ID: {task_id}"
            )

        time.sleep(_POLL_INTERVAL_SECONDS)

    raise MineruError(
        f"Conversion timed out after {_POLL_TIMEOUT_SECONDS}s. "
        f"Task ID: {task_id}"
    )


def _download_markdown(md_url: str) -> str:
    """Download the converted markdown content."""
    resp = requests.get(md_url, timeout=_REQUEST_TIMEOUT_SECONDS)
    resp.raise_for_status()
    return resp.text


# -- Public API ------------------------------------------------------------


def convert_pdf(config: ConverterConfig, pdf_path: Path) -> str:
    """Convert a local PDF file to Markdown via MinerU.

    Returns the raw markdown string.
    """
    if not pdf_path.is_file():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    print("Uploading PDF...")
    batch_id, upload_url, object_name = _request_upload_urls(config.api_token)
    _upload_pdf(upload_url, pdf_path)

    print("Converting...")
    task_id = _submit_task(
        config.api_token,
        batch_id,
        object_name,
        pdf_path.name,
        config.model,
    )
    task_data = _poll_task(config.api_token, task_id)

    print("Downloading...")
    md_url = task_data["files"][0]["md_url"]
    return _download_markdown(md_url)
