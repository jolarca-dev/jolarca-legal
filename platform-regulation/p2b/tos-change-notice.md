# P2B terms change notice — Art. 3(2) 30-day procedure + evidence

**Regulation (EU) 2019/1150, Art. 3(2): changes with ≥ 15 days' notice;
our doctrine is 30 days — the stricter standard applies to all MAJOR
legal-text changes affecting professional users.**

## Procedure

1. **Classification** — change owner classifies MAJOR/MINOR/PATCH per
   CONTRIBUTING.md; MAJOR triggers this procedure.
2. **Notice dispatch** — durable medium to affected professional users
   (in-app + email to the address on file), ≥ 30 days before the
   effective date. Notice states: what changes, why, when, and the
   termination right (Art. 3(2) second sentence: termination before the
   effective date, with our standard offboarding window).
3. **Evidence capture** — for each campaign, file here:
   `YYYY-MM-DD-<slug>/` containing dispatch list reference, message
   copy (exact version), timestamp, delivery stats.
4. **Effectivity gate** — `legal-text-sync.yml` tag for a MAJOR version
   must reference the evidence folder in the tag annotation; GC checks
   before tagging.
5. **Exception** — legal/regulatory compulsion or court order allows
   shorter notice; document the compulsion in the evidence folder.

## Templates

- `templates/notice-email.md` — professional-user notice copy skeleton.
- `templates/in-app-banner.md` — banner copy skeleton.

## Status

- [ ] Notice templates drafted
- [ ] Dispatch mechanism confirmed with product (durable medium proof)
