# DSA internal complaint handling — Art. 20 (+ P2B Art. 11/12 linkage)

**Regulation (EU) 2022/2065, Art. 20 (internal complaint-handling
system); P2B Art. 11–12 for professional users (complaint handling +
mediation).**

## Legal position

Affected users (including notifiers) must have access to a free,
electronic, easy-to-use internal complaint system for moderation
decisions, with decisions taken without automated means alone where the
complaint raises a genuine issue (Art. 20(4)). Professional users
additionally get P2B Art. 11 handling and Art. 12 mediation-body access.

## Process spec

1. Intake: linked from every statement of reasons (see
   `statement-of-reasons.md`); no re-authentication friction beyond
   account identity.
2. Human review mandatory when the complaint is substantiated with
   relevant information (Art. 20(4)) — tooling flag, reviewer identity
   logged.
3. Outcomes: uphold (reverse measure) / dismiss (reasoned). Both emit a
   new statement of reasons.
4. Deadlines: internal target ≤ 15 business days for standard cases;
   faster lanes for time-sensitive matters (funeral-related goods,
   seasonal periods).
5. Out-of-court settlement (Art. 21): certified body list maintained
   here; P2B mediation bodies (Art. 12(1)) listed for professional users.
6. Aggregated metrics feed transparency reports.

## Status

- [ ] Certified Art. 21 bodies identified per market
- [ ] P2B mediator list (Commission list reference)
- [ ] Internal SLAs approved
