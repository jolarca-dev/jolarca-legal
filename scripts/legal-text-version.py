#!/usr/bin/env python3
"""Validate legal-text front-matter and build the publish manifest.

The marketplace consumes tagged legal-text versions; this script is the
gate that keeps the front-matter schema honest.

Usage:
    legal-text-version.py --validate
    legal-text-version.py --manifest > publish-manifest.json
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEGAL_TEXTS = REPO_ROOT / "legal-texts"
LANGUAGES = ("en", "lt", "lv", "et")
STATUSES = ("draft", "approved", "effective", "superseded")
REQUIRED_KEYS = (
    "text",
    "language",
    "version",
    "status",
    "effective_date",
    "approved_by",
    "supersedes",
)
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_front_matter(path: Path) -> dict[str, str] | None:
    """Parse a simple `key: value` YAML front-matter block (stdlib only)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    meta: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return meta
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return None
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return None  # closing '---' never found


def iter_text_files():
    for family in sorted(p for p in LEGAL_TEXTS.iterdir() if p.is_dir()):
        for lang in LANGUAGES:
            lang_dir = family / lang
            if not lang_dir.is_dir():
                continue
            for md in sorted(lang_dir.glob("*.md")):
                if md.name in ("README.md", "CHANGELOG.md"):
                    continue
                yield family.name, lang, md


def validate() -> list[str]:
    errors: list[str] = []
    found = False
    for family, lang, path in iter_text_files():
        found = True
        rel = path.relative_to(REPO_ROOT)
        meta = parse_front_matter(path)
        if meta is None:
            errors.append(f"{rel}: missing or malformed front-matter block")
            continue
        for key in REQUIRED_KEYS:
            if key not in meta:
                errors.append(f"{rel}: missing front-matter key '{key}'")
        if meta.get("text") and meta["text"] != family:
            errors.append(f"{rel}: text '{meta['text']}' != folder '{family}'")
        if meta.get("language") and meta["language"] != lang:
            errors.append(f"{rel}: language '{meta['language']}' != folder '{lang}'")
        version = meta.get("version", "")
        if version and not SEMVER_RE.match(version):
            errors.append(f"{rel}: version '{version}' is not SemVer")
        status = meta.get("status", "")
        if status and status not in STATUSES:
            errors.append(f"{rel}: status '{status}' not in {STATUSES}")
        effective = meta.get("effective_date", "")
        if status == "effective" and not effective:
            errors.append(f"{rel}: status 'effective' requires effective_date")
        if effective and not DATE_RE.match(effective):
            errors.append(f"{rel}: effective_date '{effective}' is not ISO 8601")
    if not found:
        errors.append("no legal-text files found under legal-texts/")
    return errors


def manifest() -> dict:
    texts = []
    for family, lang, path in iter_text_files():
        meta = parse_front_matter(path) or {}
        texts.append(
            {
                "text": family,
                "language": lang,
                "version": meta.get("version", ""),
                "status": meta.get("status", ""),
                "effective_date": meta.get("effective_date", ""),
                "path": str(path.relative_to(REPO_ROOT)),
            }
        )
    return {
        "generated": datetime.date.today().isoformat(),
        "source_repo": "jolarca-legal",
        "texts": texts,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--validate", action="store_true",
                       help="validate front-matter of all legal texts")
    group.add_argument("--manifest", action="store_true",
                       help="emit the publish manifest as JSON")
    args = parser.parse_args()

    if args.validate:
        errors = validate()
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        if errors:
            return 1
        print("legal-text front-matter: OK")
        return 0

    print(json.dumps(manifest(), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
