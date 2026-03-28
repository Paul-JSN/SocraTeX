"""Format raw MinerU markdown into structured chapter files."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict


class FormatterError(Exception):
    """Raised when formatting or writing chapter files fails."""


class ChapterSummary(TypedDict):
    file_count: int
    title: str
    chapter_names: list[str]


@dataclass(frozen=True)
class Chapter:
    number: int
    title: str
    slug: str
    body: str


# -- LaTeX normalisation ---------------------------------------------------


_INLINE_LATEX_RE = re.compile(
    r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", re.DOTALL
)
_BLOCK_LATEX_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)


def _normalize_inline_latex(match: re.Match[str]) -> str:
    content = match.group(1).strip()
    return f"${content}$"


def _normalize_block_latex(match: re.Match[str]) -> str:
    content = match.group(1).strip()
    return f"$$\n{content}\n$$"


def normalize_latex(text: str) -> str:
    """Ensure $...$ and $$...$$ are properly whitespace-formatted."""
    result = _BLOCK_LATEX_RE.sub(_normalize_block_latex, text)
    result = _INLINE_LATEX_RE.sub(_normalize_inline_latex, result)
    return result


# -- Chapter splitting -----------------------------------------------------

_HEADING_RE = re.compile(r"^(#{1,2})\s+(.+)$", re.MULTILINE)


def _slugify(text: str) -> str:
    slug = text.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug.strip("-")[:60]


def _split_into_chapters(markdown: str) -> list[Chapter]:
    """Split markdown at top-level headings (# or ##) into chapters."""
    headings = list(_HEADING_RE.finditer(markdown))

    if not headings:
        return [Chapter(number=1, title="Full Text", slug="full-text", body=markdown)]

    chapters: list[Chapter] = []

    # Content before the first heading becomes a preamble chapter
    preamble = markdown[: headings[0].start()].strip()
    if preamble:
        chapters.append(
            Chapter(number=1, title="Preamble", slug="preamble", body=preamble)
        )

    for idx, heading_match in enumerate(headings):
        start = heading_match.start()
        end = headings[idx + 1].start() if idx + 1 < len(headings) else len(markdown)
        title = heading_match.group(2).strip()
        body = markdown[start:end].strip()
        chapter_num = len(chapters) + 1
        chapters.append(
            Chapter(
                number=chapter_num,
                title=title,
                slug=_slugify(title),
                body=body,
            )
        )

    return chapters


# -- Title extraction ------------------------------------------------------


def _extract_title(markdown: str) -> str:
    first_heading = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    if first_heading:
        return first_heading.group(1).strip()
    return "Untitled Textbook"


# -- File writing ----------------------------------------------------------


def _chapter_filename(chapter: Chapter) -> str:
    return f"ch{chapter.number:02d}-{chapter.slug}.md"


def _build_index(title: str, chapters: list[Chapter]) -> str:
    lines = [f"# {title}", "", "## Table of Contents", ""]
    for ch in chapters:
        filename = _chapter_filename(ch)
        lines.append(f"- [{ch.title}]({filename})")
    lines.append("")
    return "\n".join(lines)


def _write_chapter_file(output_dir: Path, chapter: Chapter) -> Path:
    filename = _chapter_filename(chapter)
    filepath = output_dir / filename
    filepath.write_text(chapter.body, encoding="utf-8")
    return filepath


# -- Public API ------------------------------------------------------------


def format_and_save(
    markdown: str,
    output_dir: Path,
) -> ChapterSummary:
    """Split markdown into chapters, normalise LaTeX, and write files.

    Returns a summary dict with file_count, title, and chapter_names.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    normalized = normalize_latex(markdown)
    title = _extract_title(normalized)
    chapters = _split_into_chapters(normalized)

    for chapter in chapters:
        _write_chapter_file(output_dir, chapter)

    index_content = _build_index(title, chapters)
    index_path = output_dir / "index.md"
    index_path.write_text(index_content, encoding="utf-8")

    return ChapterSummary(
        file_count=len(chapters) + 1,  # chapters + index
        title=title,
        chapter_names=[ch.title for ch in chapters],
    )
