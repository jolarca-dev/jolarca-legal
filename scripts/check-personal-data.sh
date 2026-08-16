#!/usr/bin/env bash
# check-personal-data.sh — PII tripwire for the legal repository.
#
# Privilege ≠ PII-free: privileged material routinely contains personal
# data. This scan flags patterns that should almost never land in git
# (Baltic national IDs, IBANs). It is a TRIPWIRE, not a license — a
# passing scan does not make a commit lawful (see CONTRIBUTING.md).
#
# Exits non-zero on hits so pre-commit/CI block the change for review.

set -euo pipefail

# Patterns (ERE). National-ID shapes: LT/EE 11-digit personal codes,
# LV personas kods DDMMYY-NNNNN; IBAN with country prefix.
LT_EE_PERSONAL_CODE='\b[1-6][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])[0-9]{4}\b'
LV_PERSONAL_CODE='\b[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])-[0-9]{5}\b'
IBAN='\b[A-Z]{2}[0-9]{2}[[:space:]]?([A-Z0-9][[:space:]]?[A-Z0-9]){4,30}\b'

scan() {
  local pattern="$1" label="$2" hits
  if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    if git rev-parse --verify HEAD >/dev/null 2>&1; then
      hits=$(git grep -I -n -E "$pattern" -- '*.md' '*.csv' '*.txt' '*.yml' '*.yaml' 2>/dev/null || true)
    else
      # No commits yet: scan the index (staged content).
      hits=$(git grep --cached -I -n -E "$pattern" -- '*.md' '*.csv' '*.txt' '*.yml' '*.yaml' 2>/dev/null || true)
    fi
  else
    hits=$(grep -rInE "$pattern" --include='*.md' --include='*.csv' \
      --include='*.txt' --include='*.yml' --include='*.yaml' . 2>/dev/null \
      | grep -v '^\./\.git/' || true)
  fi
  if [ -n "$hits" ]; then
    echo "POSSIBLE $label found (review each hit — false positives are possible):"
    echo "$hits"
    echo ""
    return 1
  fi
  return 0
}

fail=0
scan "$LT_EE_PERSONAL_CODE" "LT/EE national personal code" || fail=1
scan "$LV_PERSONAL_CODE" "LV personas kods" || fail=1
scan "$IBAN" "IBAN / bank account" || fail=1

if [ "$fail" -ne 0 ]; then
  echo "Personal-data pattern scan: FAIL — remove or replace with a custody"
  echo "pointer (see CONTRIBUTING.md minimization rules). If a hit is a"
  echo "legitimate load-bearing value, seek GC sign-off before committing."
  exit 1
fi
echo "personal-data pattern scan: OK (tripwire only — minimization still applies)"
