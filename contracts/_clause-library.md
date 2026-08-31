# Clause library — approved fallback positions

GC-approved positions for negotiation. Use the strongest position first;
concede down the ladder only with the noted approval. Positions marked
**no-concede** require GC decision before any movement — record the
decision in the instrument's `metadata.md`.

> Templates in `00-templates/` reference this library by clause ID (CL-xx).
> This file is High-risk class: changes require GC review + changelog note.

## Liability

| ID | Position | Notes |
|----|----------|-------|
| CL-01 | Cap at 12 months' fees paid/payable | Standard for vendors |
| CL-02 | Carve-outs uncapped: confidentiality, IP infringement, data protection, willful misconduct | no-concede below this set |
| CL-03 | No consequential damages | Both directions |
| CL-04 | Consumer-facing caps follow mandatory consumer law | Never contract out of CRD/GPSR mandatory rights |

## Governing law & forum

| ID | Position | Notes |
|----|----------|-------|
| CL-10 | Lithuanian law + Vilnius courts (B2B) | Fallback for counterparties w/ no strong preference |
| CL-11 | Accept counterparty home law only with counsel review of that venue | Record review in metadata.md |
| CL-12 | Arbitration: not preferred; acceptable only LCIA/SCC, English | no-concede on ad hoc |

## Data protection

| ID | Position | Notes |
|----|----------|-------|
| CL-20 | JOL DPA template (controller→processor) is our paper | dpa-controller-processor.md |
| CL-21 | SCCs Module per roles; no pre-2021 SCCs | Tie to jolarca-compliance TIA |
| CL-22 | Sub-processor notification + right to object (30 days) | |
| CL-23 | Breach notification to JOL ≤ 48 hours | Supports our 72h GDPR clock |

## Term & termination

| ID | Position | Notes |
|----|----------|-------|
| CL-30 | Initial term ≤ 12 months, then rolling with ≤ 60-day notice | Avoid lock-in |
| CL-31 | Termination for insolvency/material breach: 30-day cure | |
| CL-32 | Data return/destruction on exit: 30 days, certified | |

## IP

| ID | Position | Notes |
|----|----------|-------|
| CL-40 | Work product: full assignment to JOL on creation | Contractors/partners |
| CL-41 | Background IP: license only, scoped to the engagement | |
| CL-42 | License grants to JOL: perpetual, irrevocable, worldwide | For embedded third-party content |

## Payments & taxes

| ID | Position | Notes |
|----|----------|-------|
| CL-50 | Net-30 unless counterparty insists; no prepayment > 1 month | |
| CL-51 | Prices exclusive of VAT; invoice must show VAT ID | LT/OSS mechanics |

## Change log

<!-- Every position change: date, clause, old → new, approver. -->
