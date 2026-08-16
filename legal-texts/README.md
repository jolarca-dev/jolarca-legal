# legal-texts/ — Canonical marketplace legal texts

**The product consumes these files.** `jol-m-marketplace` pins versions
from here; nothing in the product's legal surfaces may diverge from a
pinned version. Legal texts are versioned build artifacts, not CMS content
(ADR-0001).

## Texts

| Text | Public audience | Key regimes |
|------|-----------------|-------------|
| `terms-of-service/` | all users | P2B (professionals), CRD, DSA basics |
| `privacy-policy/` | all users | GDPR Art. 13/14 layered notice |
| `cookie-policy/` | all users | ePrivacy + consent-banner contract (gdpr_middleware) |
| `seller-agreement/` | sellers (traders) | P2B, DSA Art. 30 KYB, commission/payouts |
| `buyer-terms/` | buyers (consumers) | CRD 14-day withdrawal + exceptions, returns |
| `community-standards/` | all users | DSA moderation basis, prohibited/sacred-goods rules |
| `imprint/` | visitors | LT/LV/EE e-commerce disclosure duties |

## Versioning doctrine (binding)

- **SemVer per text**, recorded in each file's front-matter.
- MAJOR = material term change → **P2B 30-day notice** for affected
  professional users; evidence archived under
  `platform-regulation/p2b/tos-change-notice.md` before the tag.
- MINOR = rights/obligations change; PATCH = no change of meaning.
- **Published versions are never rewritten.** Corrections ship as a new
  PATCH with a changelog entry explaining them.
- Each text keeps a plain-language `CHANGELOG.md` — this is the
  notice-to-users evidence, written for users, not lawyers.

## Front-matter schema (validated by CI)

```yaml
---
text: terms-of-service      # matches the family folder name
language: en                # en | lt | lv | et (ru reserved)
version: 0.1.0              # SemVer
status: draft               # draft | approved | effective | superseded
effective_date: ""          # ISO 8601 once effective; "" until then
approved_by: ""             # role, e.g. general-counsel
supersedes: ""              # prior version if any
---
```

`scripts/legal-text-version.py --validate` enforces the schema;
`--manifest` builds the publish manifest consumed by `legal-text-sync.yml`.

## Per-language policy

- `en/` is the drafting language and holds the canonical skeleton now.
- `lt/ lv/ et/` folders are reserved; translated files land when
  commissioned, carrying the same front-matter schema and the SAME version
  number as the source text they translate. The LT text prevails for LT
  consumers where mandatory local-language rules apply.
- `ru/` is not created; it lands only with an explicit market decision.
- Translation consistency is legally load-bearing: cross-language term
  equivalents live in [`docs/glossary.md`](../docs/glossary.md).

## Publication pipeline

1. Text changes merge to `main` (status `approved`, effective date set).
2. GC tags `legal-texts-vX.Y.Z` (tag annotation links P2B notice evidence
   for MAJOR bumps).
3. `legal-text-sync.yml` validates, builds the manifest, cross-checks the
   consent registry (`jol-m-compliance/lawful-basis`), and opens the
   marketplace PR pinning the new versions.

Consent recorded against an old privacy/cookie version must be
re-evaluated when the text changes materially — that is what the
cross-check script guards.
