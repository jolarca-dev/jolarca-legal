# powers-of-attorney/ — Signing authority instruments

Who may sign what, evidenced.

- One file per PoA: grantor, attorney, scope, value limits, expiry,
  grant date, notarial reference (where notarized).
- `revocation-log.md` — every revocation: date, reason category
  (role change / expiry / cause), notified parties. A revoked PoA is
  never deleted; it is marked revoked and cross-linked.

Invariants:

- The live summary is
  [`docs/signing-authority-matrix.md`](../../docs/signing-authority-matrix.md);
  it must match this folder on every change (same-day update rule).
- Dual-signature thresholds are defined in the matrix, not here.
