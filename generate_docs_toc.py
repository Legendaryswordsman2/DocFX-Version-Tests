#!/usr/bin/env python3
"""
DocFX TOC builder/updater (with formatting preserved)

- Scans ./docs for .md files and mirrors folder structure in docs/toc.yml
- If toc.yml exists, it:
  * keeps existing entry order
  * preserves *existing names* as long as their href still points to a real file
  * removes entries whose relative .md href no longer exists
  * adds missing files (without duplicating existing hrefs)
  * does NOT change names you manually edited
  * preserves formatting, indentation, and comments
"""

from __future__ import annotations
import os
from pathlib import Path, PurePosixPath
from typing import Any, Dict, List, Optional, Set

from ruamel.yaml import YAML

DOCS_DIR = Path(__file__).parent / "docs"
TOC_PATH = DOCS_DIR / "toc.yml"

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True

# ---------------------------- helpers ----------------------------

def to_posix_rel(path: Path, base: Path) -> str:
    return str(PurePosixPath(path.relative_to(base).as_posix()))

def normalize_href_for_fs(href: str) -> Optional[str]:
    if not isinstance(href, str):
        return None
    href = href.strip()
    if not href:
        return None

    lowered = href.lower()
    if lowered.startswith(("http://", "https://", "mailto:")) or href.startswith("/"):
        return None

    if "#" in href:
        href = href.split("#", 1)[0].strip()

    if not href.endswith(".md"):
        return None

    while href.startswith("./"):
        href = href[2:]

    return str(PurePosixPath(href))

def format_name_from_filename(filename: str) -> str:
    name = Path(filename).stem
    return name.replace("-", " ").replace("_", " ").title()

def list_markdown_files(base: Path) -> List[Path]:
    return sorted(p for p in base.rglob("*.md") if p.is_file())

def load_existing_toc(path: Path):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        data = yaml.load(f)
    if not data:
        return []
    if not isinstance(data, list):
        raise SystemExit("toc.yml must be a YAML list at the top level.")
    return data

def dump_toc(path: Path, toc) -> None:
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(toc, f)

# ------------------------- TOC operations ------------------------

def collect_all_hrefs(toc) -> Set[str]:
    out: Set[str] = set()
    for entry in toc:
        href = entry.get("href")
        if isinstance(href, str):
            norm = normalize_href_for_fs(href)
            if norm:
                out.add(norm)
        if isinstance(entry.get("items"), list):
            out.update(collect_all_hrefs(entry["items"]))
    return out

def prune_invalid_hrefs_inplace(toc, docs_dir: Path) -> None:
    i = 0
    while i < len(toc):
        entry = toc[i]
        href = entry.get("href")
        items = entry.get("items")

        removed = False
        if isinstance(href, str):
            norm = normalize_href_for_fs(href)
            if norm and not (docs_dir / norm).exists():
                toc.pop(i)
                removed = True
        if not removed and isinstance(items, list):
            prune_invalid_hrefs_inplace(items, docs_dir)
        if not removed:
            i += 1

def ensure_folder_chain(entries, dir_parts: List[str], current_path: str = ""):
    if not dir_parts:
        return entries

    target_dir = "/".join([p for p in [current_path, dir_parts[0]] if p])

    for e in entries:
        items = e.get("items")
        if isinstance(items, list) and subtree_has_prefix(items, target_dir + "/"):
            return ensure_folder_chain(items, dir_parts[1:], target_dir)

    for e in entries:
        items = e.get("items")
        if isinstance(items, list) and isinstance(e.get("name"), str):
            if e["name"].strip().lower() == format_name_from_filename(dir_parts[0]).lower():
                return ensure_folder_chain(items, dir_parts[1:], target_dir)

    new_header = {"name": format_name_from_filename(dir_parts[0]), "items": []}
    entries.append(new_header)
    return ensure_folder_chain(new_header["items"], dir_parts[1:], target_dir)

def subtree_has_prefix(entries, prefix: str) -> bool:
    for e in entries:
        href = e.get("href")
        if isinstance(href, str):
            norm = normalize_href_for_fs(href)
            if norm and norm.startswith(prefix):
                return True
        items = e.get("items")
        if isinstance(items, list) and subtree_has_prefix(items, prefix):
            return True
    return False

def href_exists_anywhere(toc, target_norm: str) -> bool:
    for e in toc:
        href = e.get("href")
        if isinstance(href, str):
            norm = normalize_href_for_fs(href)
            if norm == target_norm:
                return True
        items = e.get("items")
        if isinstance(items, list) and href_exists_anywhere(items, target_norm):
            return True
    return False

def add_missing_files(toc, docs_dir: Path) -> None:
    all_md = list_markdown_files(docs_dir)
    for md in all_md:
        rel = to_posix_rel(md, docs_dir)
        if href_exists_anywhere(toc, rel):
            continue
        parts = rel.split("/")
        dirs, filename = parts[:-1], parts[-1]
        container = ensure_folder_chain(toc, dirs)
        container.append({
            "name": format_name_from_filename(filename),
            "href": rel,
        })

# ---------------------------- main -------------------------------

def main() -> None:
    if not DOCS_DIR.exists():
        raise SystemExit(f"Docs folder not found: {DOCS_DIR}")

    toc = load_existing_toc(TOC_PATH)
    prune_invalid_hrefs_inplace(toc, DOCS_DIR)
    add_missing_files(toc, DOCS_DIR)
    dump_toc(TOC_PATH, toc)

    total = len(collect_all_hrefs(toc))
    print(f"Updated {TOC_PATH} with {total} markdown entries.")

if __name__ == "__main__":
    main()