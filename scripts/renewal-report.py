#!/usr/bin/env python3
"""Parse contract registers and report upcoming renewals / notice windows.

Registers: contracts/**/_register.csv (fixed schema). Rows starting with
'#' are documentation and skipped.

Usage:
    renewal-report.py                    # human report, 90-day window
    renewal-report.py --days 30          # human report, custom window
    renewal-report.py --json --days 90   # machine-readable (CI/workflows)
    renewal-report.py --check-register   # schema/parse validation gate
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPECTED_COLUMNS = [
    "contract_id",
    "counterparty",
    "instrument_class",
    "value_amount",
    "value_currency",
    "start_date",
    "end_date",
    "auto_renew",
    "notice_days",
    "owner",
    "status",
]
STATUSES = ("draft", "negotiation", "approved", "executed", "expired", "terminated")


def find_registers() -> list[Path]:
    return sorted(REPO_ROOT.glob("contracts/**/_register.csv"))


def parse_date(value: str) -> datetime.date:
    return datetime.date.fromisoformat(value)


def load_rows(register: Path) -> list[dict[str, str]]:
    with register.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(
                f"{register}: header mismatch — expected {EXPECTED_COLUMNS}, "
                f"got {reader.fieldnames}"
            )
        return [row for row in reader if not row["contract_id"].startswith("#")]


def check_registers() -> list[str]:
    errors: list[str] = []
    registers = find_registers()
    if not registers:
        return ["no contracts/**/_register.csv found"]
    for register in registers:
        try:
            rows = load_rows(register)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        for row in rows:
            cid = row["contract_id"]
            for field in ("start_date", "end_date"):
                try:
                    parse_date(row[field])
                except ValueError:
                    errors.append(f"{cid}: {field} '{row[field]}' is not ISO 8601")
            if not row["notice_days"].isdigit():
                errors.append(f"{cid}: notice_days '{row['notice_days']}' not an integer")
            if row["auto_renew"] not in ("yes", "no"):
                errors.append(f"{cid}: auto_renew must be yes|no")
            if row["status"] not in STATUSES:
                errors.append(f"{cid}: status '{row['status']}' not in {STATUSES}")
    return errors


def upcoming(days: int) -> list[dict]:
    today = datetime.date.today()
    horizon = today + datetime.timedelta(days=days)
    items = []
    for register in find_registers():
        for row in load_rows(register):
            if row["status"] not in ("executed", "approved"):
                continue
            end = parse_date(row["end_date"])
            if end > horizon:
                continue
            notice_days = int(row["notice_days"]) if row["notice_days"].isdigit() else 0
            notice_deadline = end - datetime.timedelta(days=notice_days)
            items.append(
                {
                    "contract_id": row["contract_id"],
                    "counterparty": row["counterparty"],
                    "instrument_class": row["instrument_class"],
                    "end_date": row["end_date"],
                    "auto_renew": row["auto_renew"],
                    "notice_days": notice_days,
                    "notice_deadline": notice_deadline.isoformat(),
                    "owner": row["owner"],
                    "days_left": (end - today).days,
                    "notice_days_left": (notice_deadline - today).days,
                }
            )
    items.sort(key=lambda item: item["notice_days_left"])
    return items


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=90,
                        help="look-ahead window in days (default 90)")
    parser.add_argument("--json", action="store_true",
                        help="machine-readable output")
    parser.add_argument("--check-register", action="store_true",
                        help="validate register schema and rows")
    args = parser.parse_args()

    if args.check_register:
        errors = check_registers()
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        if errors:
            return 1
        print("contract registers: OK")
        return 0

    items = upcoming(args.days)
    if args.json:
        print(json.dumps(items, indent=2))
        return 0

    if not items:
        print(f"No renewals or notice windows within {args.days} days.")
        return 0
    print(f"Renewals & notice windows — next {args.days} days:")
    for item in items:
        flag = "NOTICE WINDOW OPEN" if item["notice_days_left"] <= 0 else "notice ahead"
        print(
            f"  {item['contract_id']:<16} {item['counterparty']:<24} "
            f"ends {item['end_date']} (in {item['days_left']}d) | "
            f"notice by {item['notice_deadline']} [{flag}] | owner: {item['owner']}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
