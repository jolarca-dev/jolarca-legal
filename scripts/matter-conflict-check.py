#!/usr/bin/env python3
"""Counsel conflict-of-interest pre-check against the counterparty record.

Before engaging new counsel (or accepting a matter against a new
counterparty), check the name against: executed contract counterparties,
dispute matter registers, and the opinions index. A hit means "verify
manually before proceeding", never "automatically blocked".

Usage:
    matter-conflict-check.py "Counterparty Name"
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTER_SOURCES = list(REPO_ROOT.glob("contracts/**/_register.csv"))
TEXT_SOURCES = [
    REPO_ROOT / "disputes" / "_register.md",
    REPO_ROOT / "opinions" / "_index.md",
]


def check_registers(name: str) -> list[str]:
    hits = []
    needle = name.lower()
    for register in REGISTER_SOURCES:
        with register.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                cid = row.get("contract_id", "")
                if cid.startswith("#"):
                    continue
                if needle in row.get("counterparty", "").lower():
                    hits.append(f"{register.relative_to(REPO_ROOT)}: {cid} "
                                f"({row.get('counterparty')}, status "
                                f"{row.get('status')})")
    return hits


def check_text_files(name: str) -> list[str]:
    hits = []
    needle = name.lower()
    for source in TEXT_SOURCES:
        if not source.is_file():
            continue
        for lineno, line in enumerate(
            source.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if needle in line.lower():
                hits.append(f"{source.relative_to(REPO_ROOT)}:{lineno}")
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("counterparty", help="counterparty or counsel name")
    args = parser.parse_args()

    hits = check_registers(args.counterparty) + check_text_files(args.counterparty)
    if not hits:
        print(f"no conflict record found for '{args.counterparty}' "
              "(verify independence manually; absence of record is not "
              "assurance)")
        return 0

    print(f"potential conflict records for '{args.counterparty}':")
    for hit in hits:
        print(f"  - {hit}")
    print("Counsel decision required before engagement — do not proceed "
          "on automation alone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
