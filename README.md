# jolarca-legal — Legal Function Repository

**Private** repository of record for the Journey of Life marketplace legal
function (`jol-m-*` fleet). Corporate governance, contract lifecycle,
marketplace legal texts, EU platform-regulation compliance, IP, disputes,
and regulatory correspondence live here.

> **Privilege rule:** material marked *privileged* (disputes, inquiries,
> opinions) is work product of, or prepared for, counsel. It must never be
> copied, quoted, or summarized into any other repository, issue tracker,
> chat, or product artifact. See [disputes/README.md](disputes/README.md).

## What this repository is

- **Canonical source** for marketplace legal texts (`legal-texts/`). The
  product (`jolarca`) consumes versioned, tagged releases — legal
  texts are build artifacts, not CMS content (ADR-0001).
- **Contract lifecycle management (CLM)** for vendors, customers,
  partnerships, and employment (`contracts/`), with a machine-readable
  register that drives renewal automation.
- **EU platform-regulation program** (DSA, P2B, GPSR, consumer law, VAT/OSS)
  — the marketplace-specific legal core (`platform-regulation/`).
- Corporate records, IP portfolio, regulatory correspondence, disputes,
  insurance, and legal opinions.

Cross-repo boundaries: GDPR evidence (RoPA, DPIAs-as-records, lawful-basis
registry, DSAR logs) lives in `jolarca-compliance`; this repository holds the
legal instruments and analysis. Dispute outcomes feed
`jolarca-compliance/risk-register`.

## Privilege & access rules

| Rule | Enforcement |
|------|-------------|
| General counsel (GC) owns `executed` paths and all legal texts | CODEOWNERS on `legal-texts/`, `contracts/` (§3) |
| Privileged material = GC + retained counsel only | CODEOWNERS on `disputes/`, `regulatory/inquiries/`; repo visibility |
| No personal data unless load-bearing and minimized | pre-commit pattern scan (privilege ≠ PII-free), gitleaks |
| Executed versions are immutable | versioning doctrine in [CONTRIBUTING.md](CONTRIBUTING.md) |

## Counsel directory

| Role | Contact | Scope |
|------|---------|-------|
| General counsel (owner) | TBD — fill on onboarding | All areas; signing authority matrix in `docs/signing-authority-matrix.md` |
| Retained litigation counsel | TBD | `disputes/` matters only |
| Data-protection counsel | TBD | GDPR/DSA interface with `jolarca-compliance` |
| IP agent (EUIPO filings) | TBD | `intellectual-property/trademarks/` |

## Request intake & SLAs

Intake is issue-based (see `.github/ISSUE_TEMPLATE/`):

| Request type | Template | Triage | First substantive response |
|--------------|----------|--------|---------------------------|
| New/changed contract | `contract_request.yml` | 1 business day | 5 business days (standard tier) |
| Product/marketing review | `legal_review_request.yml` | 1 business day | 3 business days for launches; campaign copy 5 |
| Regulatory change | `regulatory_change.yml` | 2 business days | Impact assessment scoped in 10 business days |
| Authority inquiry / claim | `regulatory/inquiries/` intake | same day | Counsel engaged within 1 business day |
| Active litigation threat | SECURITY.md escalation | immediate | Counsel + insurer (breach coach) notified first |

## Repository map

| Path | Purpose |
|------|---------|
| `corporate/` | UAB formation, board records, cap table, PoA, registrations |
| `contracts/` | CLM: templates, executed instruments, clause library, register |
| `legal-texts/` | Canonical marketplace texts, SemVer per text, per-language |
| `platform-regulation/` | DSA, P2B, GPSR, consumer law, VAT/OSS, horizon scanning |
| `intellectual-property/` | Trademarks, domains, copyright/CLA, trade secrets |
| `regulatory/` | Supervisory authorities, consumer protection, tax, inquiries |
| `disputes/` | Matters (highest restriction), matter register |
| `insurance/` | Policies, panel firms, claims register |
| `opinions/` | Legal memos and opinions, searchable index |
| `docs/` | Architecture, ADRs, glossary, signing-authority matrix, retention |
| `scripts/` | Renewal reports, text-version validation, consent cross-check |
| `audits/` | Internal audit records for this repository |

## Quickstart (legal operators)

```bash
make check          # front-matter + register + governance gates
make lint-docs      # markdown/YAML hygiene
make versions       # legal-text version manifest (what ships to product)
make renewal-report # upcoming renewals & notice windows from contracts register
```

Renewal automation (`contract-renewals.yml`) opens tasks at 90/60/30 days
before expiry or notice deadlines. Legal-text releases are tagged;
`legal-text-sync.yml` publishes versions to `jolarca` and the
consent registry.

## Change discipline

Redlines are preserved, executed versions are immutable, and every term
change is auditable through Conventional Commits + CHANGELOG (see
[CONTRIBUTING.md](CONTRIBUTING.md)). Incidents involving legal data are the
highest severity class: counsel is notified first ([SECURITY.md](SECURITY.md)).
