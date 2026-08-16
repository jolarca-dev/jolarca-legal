# Signing authority matrix

Who may sign for UAB "Journey of Life", at what value, and with whose
countersignature. Underlying instruments: `corporate/powers-of-attorney/`.
This matrix must be updated the same day any PoA changes (CODEOWNERS: GC).

## Authority tiers

| Tier | Value threshold (per instrument) | Signatories | Countersignature |
|------|----------------------------------|-------------|------------------|
| T1 — routine | ≤ €5,000 | director or PoA holder (scope-limited) | none |
| T2 — standard | €5,000–€25,000 | director | GC review record in metadata.md |
| T3 — material | €25,000–€100,000 | director | GC + finance |
| T4 — significant | > €100,000, or multi-year > €50k/yr | director + board authorization | board resolution reference |
| T5 — reserved | IP assignments, cap-table, real estate, guarantees | director + board resolution | board resolution + GC |

## Dual-signature rules

- Any single instrument > €50,000 requires dual signature (director +
  one authorized officer) regardless of tier classification.
- Employment contracts: director (or delegated HR officer per PoA);
  compensation terms follow `contracts/employment/` restrictions.
- Legal texts are not "signed" — publication is effected by GC tag +
  pipeline; the tag is the authority act (recorded in git).

## Standing limitations

- PoA holders may not sign contracts with themselves or their own
  entities (conflict rule; exceptions need board approval).
- Notices that create/terminate obligations (contract non-renewal
  notices, P2B notices) are signed at T2 minimum regardless of value.

## Register linkage

Every signature act on a registered instrument updates
`contracts/**/_register.csv` status the same day.
