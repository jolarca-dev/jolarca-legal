# License compliance — third-party dependency audit procedure

Keeps the AGPL-3.0 codebase clean and the marketplace legally distributable.

## Procedure

1. **SBOM per release** — code repos generate an SBOM (CycloneDX/SPDX)
   in CI; the SBOM is the audit input.
2. **License classification** — every dependency falls into:
   - **Green:** MIT/BSD/Apache-2.0 etc. — attribute per license text.
   - **Amber:** LGPL/MPL/weak copyleft — usage pattern checked (dynamic
     linking / separable module) before merge.
   - **Red:** GPL/AGPL in non-AGPL components, SSPL, BUSL, Commons
     Clause — blocked; exceptions require GC + engineering lead sign-off
     recorded in an ADR in the code repo.
3. **Audit cadence** — full sweep quarterly + on every major framework
   upgrade; results recorded as `audit-YYYY-Qn.md` in the code repo's
   compliance folder, linked here.
4. **Attribution surface** — product must expose license notices
   (third-party notices page); its content is generated from the SBOM.

## Escalation

Discovery of an unlicensed or mislicensed dependency in production:
engineering incident + this folder get same-day entries; GC decides
remediation (remove / replace / commercial license).
