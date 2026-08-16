# registrations/ — Statutory registrations & filings

One folder per regime. Each registration file records: filing date,
authority reference, current status, renewal/refiling obligation, and the
responsible person.

Expected regimes:

| Folder | Regime | Authority |
|--------|--------|-----------|
| `vat/` | LT VAT payer registration | VMI (State Tax Inspectorate) |
| `oss/` | EU One-Stop-Shop VAT registration | VMI (OSS portal) |
| `eori/` | EORI number (if customs activity) | LT Customs |
| `lei/` | Legal Entity Identifier + renewal | LOU / agent |
| `jar/` | Register of Legal Entities filings | Registrų centras |
| `other/` | Licenses/permits as acquired | varies |

Scanned apostille/notarization certificates file here with the filing
reference in the filename. Renewal dates feed the manual review cadence
(listed in each regime's file; no automation — filings are rare and
consequential).
