# Security Policy — jol-m-legal

## Severity doctrine

**Any incident involving legal data in this repository is the highest
severity class.** Legal exposure compounds technical exposure: a leaked
dispute file or executed contract can destroy privilege, weaken a live
matter, and trigger regulatory notification duties.

**Counsel is notified first** — before or in parallel with the security
function, never after. Order of notification:

1. General counsel (repo owner) — immediately.
2. Retained counsel for the affected matter (if matter-specific).
3. Security function / incident commander (`jol-m-infrastructure` runbooks).
4. Insurer breach coach (cyber policy — `insurance/cyber/`) if personal
   data or third-party instruments are involved.
5. DPO (`jol-m-compliance`) if personal data is involved — GDPR 72h clock
   assessment starts with the DPO, not with this repository.

## Reporting

**NEVER open issues about legal-data incidents in any public or shared
repository.** Use the org security mailbox + direct counsel contact.

Include: affected path(s), how the exposure was discovered, suspected
blast radius (which instruments/matters/personal data), and whether the
material left the repository (clone, paste, screenshot, e-sign export).

## What we treat as a security incident

- Any privileged material (`disputes/`, `regulatory/inquiries/`,
  `opinions/` marked privileged) appearing outside this repository —
  including summaries or paraphrases in other repos, issues, or chat.
- Any executed contract or corporate record appearing outside its custody
  location (including e-signature envelope exports and signed-PDF caches).
- Any personal data committed beyond what is load-bearing (see
  CONTRIBUTING.md minimization rule) — assess under GDPR with the DPO.
- Any secret (token, API key, signing credential) in git history.
- Unauthorized access grant to this repository (check access reviews in
  `audits/`).

## Response targets

| Stage | Target |
|-------|--------|
| Counsel acknowledgement | same business day |
| Containment (revoke access, purge caches, rotate tokens) | 1 business day |
| Privilege/breach assessment | 3 business days |
| Regulatory notification decision (if personal data) | per GDPR 72h clock via DPO |

## Privilege preservation during incidents

Incident handling must not waive privilege: forensic copies of privileged
paths are made under counsel direction and labeled; third-party responders
receive only redacted, counsel-approved excerpts.

## Supported scope

Only the default branch (`main`) of this repository is supported.
