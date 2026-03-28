"""CLI entry point for the Socratex PDF converter.

Usage:
    python -m converter path/to/textbook.pdf
    socratex-convert path/to/textbook.pdf --output-dir books/ --name my-book
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from converter.config import ConfigError, load_config
from converter.formatter import FormatterError, format_and_save
from converter.mineru_client import MineruAuthError, MineruError, convert_pdf


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="socratex-convert",
        description="Convert a PDF textbook to structured Markdown chapters.",
    )
    parser.add_argument(
        "pdf",
        type=Path,
        help="Path to the PDF file to convert.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Base output directory (default: books/).",
    )
    parser.add_argument(
        "--name",
        type=str,
        default=None,
        help="Folder name for this book (default: derived from PDF filename).",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="MinerU model version (default: vlm).",
    )
    return parser


def _derive_book_name(pdf_path: Path) -> str:
    return pdf_path.stem.lower().replace(" ", "-")


def _print_summary(summary: dict[str, object], book_dir: Path) -> None:
    print("\n--- Conversion Complete ---")
    print(f"  Title:    {summary['title']}")
    print(f"  Files:    {summary['file_count']}")
    print(f"  Output:   {book_dir.resolve()}")
    print(f"  Chapters:")
    for name in summary.get("chapter_names", []):
        print(f"    - {name}")


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    pdf_path: Path = args.pdf.resolve()
    if not pdf_path.is_file():
        print(f"Error: PDF file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    if not pdf_path.suffix.lower() == ".pdf":
        print(f"Error: Expected a .pdf file, got: {pdf_path.suffix}", file=sys.stderr)
        sys.exit(1)

    try:
        config = load_config(output_dir=args.output_dir, model=args.model)
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        sys.exit(1)

    book_name = args.name or _derive_book_name(pdf_path)
    book_dir = config.output_dir / book_name

    try:
        raw_markdown = convert_pdf(config, pdf_path)
    except MineruAuthError as exc:
        print(f"Authentication error: {exc}", file=sys.stderr)
        sys.exit(1)
    except MineruError as exc:
        print(f"Conversion error: {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"Unexpected error during conversion: {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        summary = format_and_save(raw_markdown, book_dir)
    except FormatterError as exc:
        print(f"Formatting error: {exc}", file=sys.stderr)
        sys.exit(1)

    _print_summary(summary, book_dir)


if __name__ == "__main__":
    main()
