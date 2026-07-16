#!/usr/bin/env python3
"""Transform book/*.md into reader-facing copies for the Quarto build.

Each chapter file has three parts, separated by two "---" rules: a
front-matter block (H1 title + bold Part/Concept Level/Prerequisites/New
concepts metadata), the body (11 numbered sections), and a footer
bookkeeping block (glossary/misconceptions/concept-graph notes). Only the
title and body are reader-facing; the rest is authoring scaffolding that
keeps the supporting files in sync and was never meant to be read.

This script never touches book/ — it writes stripped copies to
publish/chapters/, mirroring book/'s Part directory structure, for Quarto
to render. Safe to re-run; always regenerates from the book/ source.

    python3 scripts/prepare_manuscript_for_publish.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "book"
OUT_DIR = ROOT / "publish" / "chapters"


def strip_chapter(text: str) -> str:
    parts = text.split("\n---\n")
    if len(parts) != 3:
        raise ValueError(f"expected 3 parts split on '---', got {len(parts)}")
    frontmatter, body, _footer = parts
    title_line = frontmatter.strip().splitlines()[0]
    return f"{title_line}\n\n{body.strip()}\n"


def main():
    chapter_files = sorted(BOOK_DIR.glob("part-*/*.md"))
    if not chapter_files:
        raise SystemExit(f"no chapter files found under {BOOK_DIR}")

    for src in chapter_files:
        part_dir = src.parent.name
        dest = OUT_DIR / part_dir / src.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(strip_chapter(src.read_text()))
        print(f"wrote {dest.relative_to(ROOT)}")

    print(f"\n{len(chapter_files)} chapters prepared in {OUT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
