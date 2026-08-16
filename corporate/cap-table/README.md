# cap-table/ — Ownership records

- `shareholder-register.md` — current register: holder, class, count,
  acquisition date, transfer restrictions. Updates are dated entries;
  the history stays visible (no deletions, supersede-not-erase).
- `options/` — option grants (if any): one file per grant with plan
  reference, vesting, exercise mechanics. Compensation values live in the
  sealed custody location; this tree holds grant mechanics only.

Changes here are Crit-risk class: GC + board authorization recorded
before merge (board resolution reference in the PR).
