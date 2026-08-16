# copyright/ — Open-source posture

The marketplace application code is published under **AGPL-3.0** (see
`jol-m-marketplace`). This folder governs the copyright side of that
posture.

| File | Purpose |
|------|---------|
| `cla.md` | Contributor License Agreement (canonical) |
| `license-compliance.md` | Third-party dependency audit procedure |

Rules:

- Inbound contributions require signed CLA (or DCO where the project
  accepts DCO-only contributions); the bot/branch protection state is
  tracked in the marketplace repo, the canonical text lives here.
- AGPL obligations (source availability for network use) are product
  duties — the compliance mechanism is documented in
  `license-compliance.md` and enforced in CI of the code repos.
- Contractor work product must arrive assigned (CL-40) before landing in
  AGPL code — see `contracts/00-templates/contractor-agreement.md`.
