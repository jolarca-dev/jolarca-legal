# Retention schedule

Retention classes for records in this repository. Destruction happens
only after: deadline passed AND no legal hold AND GC written approval —
the destruction itself is logged (what, when, who, authority).

| Class | Records | Retention | Authority |
|-------|---------|-----------|-----------|
| R1 | Executed contracts + amendments | term + 10 years | LT Civil Code limitation + tax |
| R2 | Corporate filings & board records | permanent | company law |
| R3 | Legal-text published versions + notice evidence | permanent (publication proof) | P2B/DSA evidence |
| R4 | Pre-contractual negotiation (unexecuted redlines) | 3 years from last activity | limitation |
| R5 | Dispute matters (closed) | closure + 10 years | limitation + appeals risk |
| R6 | Authority inquiries | closure + 10 years | as R5 |
| R7 | Legal opinions (privileged) | permanent unless GC releases | privilege survives; destruction needs counsel |
| R8 | Insurance claims | closure + 10 years | policy conditions |
| R9 | CLA records | duration of project copyright + 5 years | copyright term |
| R10 | KYB/trader verification records | relationship + 5 years | DSA Art. 30 accountability |
| R11 | Register CSVs | same as underlying instruments | derived |

## Legal holds

A hold suspends destruction for the hold scope (`disputes/`,
`regulatory/inquiries/` open a hold at intake). Hold releases are
recorded in the matter folder.

## Sweep cadence

Annual retention sweep (see `audits/`): due destructions proposed, GC
approves item-by-item, destruction logged as `audits/internal/` entry.
