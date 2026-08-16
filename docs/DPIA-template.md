# DPIA template — GDPR Art. 35

Template-inherited from the fleet baseline; legal-flavored extensions
below. **Completed DPIAs file in `jol-m-compliance/dpia/`** — this
repository keeps the template and legal-side inputs only.

**When required:** any change introducing or altering processing of
personal data (new data flow, new retention, new processor, new
analytics). Attach the completed DPIA to the change request BEFORE
implementation. Legal-text changes touching purposes/bases additionally
trigger the consent cross-check (see `legal-texts/README.md`).

---

## 1. Processing description

- Purpose of processing:
- Categories of data subjects:
- Categories of personal data (flag special categories Art. 9 —
  religious beliefs are Art. 9 data: sacred-goods and ritual features
  must be checked against this explicitly):
- Data flows (source → processing → storage → recipients):
- Legal basis (Art. 6):
- Retention period & deletion mechanism (tie to `retention-schedule.md`):

## 2. Necessity & proportionality

- Why is each data element necessary?
- Minimization measures (pseudonymization, tokenization, aggregation):
- Alternatives considered and rejected:

## 3. Risk assessment (to rights & freedoms)

| Risk scenario | Likelihood | Impact | Mitigation |
|---------------|------------|--------|------------|
|               |            |        |            |

## 4. Technical & organizational measures

- Encryption at rest / in transit:
- Access control (who, how granted, review cadence):
- Residency: EU-only unless SCCs + transfer assessment documented:
- Breach detection & notification path (72h, Art. 33 — SECURITY.md order):

## 5. Processor/sub-processor check

- New third parties introduced? List, DPA status
  (`contracts/00-templates/dpa-controller-processor.md`), location:

## 6. Legal-text impact (legal extension)

- Which legal texts change as a result (privacy/cookie/buyer-terms)?
- Version bump classification (MAJOR/MINOR/PATCH):
- Consent re-evaluation needed: yes/no:

## 7. Conclusion & sign-off

- Residual risk acceptable? (yes/no + rationale)
- DPO consulted (Art. 35.2): date / name
- Approved by: / Date:
