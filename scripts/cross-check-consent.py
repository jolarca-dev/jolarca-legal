#!/usr/bin/env python3
"""Cross-check legal-text versions against the consent registry.

Consent recorded against a privacy/cookie text version must be
re-evaluated when that text changes materially. The registry of record
is the lawful-basis registry in jolarca-compliance.

With COMPLIANCE_RO_TOKEN unset the script performs an offline sanity
check of the manifest and prints the follow-ups a live check would need;
it never fails a pipeline for a missing remote (advisory mode).

Usage:
    cross-check-consent.py --manifest publish-manifest.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

# Texts whose changes can invalidate recorded consent.
CONSENT_SENSITIVE = ("privacy-policy", "cookie-policy", "terms-of-service")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True,
                        help="path to publish manifest JSON")
    args = parser.parse_args()

    with open(args.manifest, encoding="utf-8") as fh:
        manifest = json.load(fh)

    texts = manifest.get("texts", [])
    if not texts:
        print("ERROR: manifest contains no texts", file=sys.stderr)
        return 1
    for entry in texts:
        if not entry.get("version") or not entry.get("text"):
            print(f"ERROR: incomplete manifest entry: {entry}", file=sys.stderr)
            return 1

    sensitive = sorted(
        {e["text"] for e in texts if e["text"] in CONSENT_SENSITIVE}
    )

    token = os.environ.get("COMPLIANCE_RO_TOKEN", "")
    if not token:
        print(
            "consent cross-check: COMPLIANCE_RO_TOKEN not set — offline mode.\n"
            "  Manifest OK. Consent-sensitive texts in this release: "
            f"{', '.join(sensitive) if sensitive else 'none'}.\n"
            "  TODO(legal-automation): query jolarca-compliance/lawful-basis for "
            "consent records pinned to prior versions of these texts and "
            "open a re-consent evaluation task where found."
        )
        return 0

    # Live check lands with the compliance registry API; the token branch
    # intentionally stays a stub until that contract exists.
    print("consent cross-check: token present — live registry check pending "
          "registry API contract (stub).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
