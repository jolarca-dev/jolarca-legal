# DSA trader traceability — Art. 30–32 KYB spec

**Regulation (EU) 2022/2065, Art. 30 (know-your-business-customer),
Art. 31 (compliance by design), Art. 32 (right to information).**

## Legal position

Before allowing a trader to use the marketplace, we must obtain and
verify (Art. 30(1)): name, address, contact details, trade register &
registration number (or equivalent), self-certification of compliance
with product safety/product liability law, and — where applicable — VAT
details. Art. 30(3): verification via reliable sources; Art. 30(4):
periodic re-verification attempts; Art. 30(5)/(6): suspension of
non-complying traders + transparency on that.

## Product spec hook

Implemented by the seller onboarding flow (`sellers_app` KYB):

1. Collection at onboarding (fields per Art. 30(1), per market LT/LV/EE).
2. Verification sources: national registers (LT JAR / LV UR / EE e-BR),
   VAT VIES check; document upload for non-register evidence.
3. Re-verification cadence: at least annually for active traders +
   event-driven (payment failure patterns, complaints spike).
4. Failure path: grace notice → listing restriction → suspension, each
   step emitting a statement-of-reasons (see `statement-of-reasons.md`).
5. Buyer-facing trader information display (Art. 32) on listing pages.

## Evidence & records

- KYB records retention: per `docs/retention-schedule.md`.
- Non-compliance actions feed the DSA transparency report
  (`transparency-reports/`).

## Status

- [ ] Field mapping per market approved by GC
- [ ] Verification-source list finalized (registers + VIES)
- [ ] Product flow reviewed against this spec
