# Changelog — jolarca-legal

All notable changes to this legal repository are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
commits follow Conventional Commits. Every legal-term change is auditable
— never rewrite released entries. Legal-text versions have their own
per-text changelogs under `legal-texts/<text>/CHANGELOG.md`.

## [Unreleased]

### Added

- Repository scaffold: corporate, contracts (CLM), legal-texts
  (canonical, SemVer per text), platform-regulation (DSA/P2B/GPSR/
  consumer-law/VAT-OSS/watches), intellectual-property, regulatory,
  disputes, insurance, opinions, docs, scripts, audits.
- Root compliance baseline: README (privilege rules, counsel directory,
  request SLAs), LICENSE (internal use + publication-pipeline exception),
  SECURITY.md (legal-data incidents = highest severity, counsel first),
  CONTRIBUTING.md (redlines preserved, executed versions immutable).
- CI/CD: ci + compliance-check gates, contract-renewals (90/60/30-day
  notice automation), legal-text-sync (tag → marketplace PR + consent
  registry), ip-renewals (quarterly), transparency-report-data (DSA
  semi-annual).
- Pre-commit baseline + gitleaks + personal-data pattern scan.
- Contract register (`contracts/vendors/_register.csv`) driving renewal
  automation; clause library and JOL-standard templates.
- Scripts: renewal report, legal-text version validation/manifest,
  consent-registry cross-check, matter conflict-of-interest pre-check.
- ADR-0001: legal texts as versioned build artifacts, not CMS content.
- Glossary (LT/LV/EE term equivalents), signing-authority matrix,
  retention schedule.
- Repository readiness audit (`audits/internal/2026-09-repo-readiness-gate.md`):
  15 findings across governance, access control, signing, and CI integrity;
  B-1/B-3/B-4/H-1 remediated, B-2 open on a billing decision.
- Monthly "Governance & CI integrity" cadence row in `audits/README.md` —
  closes the audit-programme blind spot where B-1 occurred.
- Unit tests wired into CI gate: `python3 -m unittest discover -s scripts/tests -v`
  runs as a required step in `ci.yml` (PR #13, closes audit finding H-3).

### Changed

- Supply chain hardened: all `uses:` directives in workflows are now SHA-pinned
  (PR #14, closes audit findings M-2 + M-3); `yamllint` pinned to exact version
  `1.38.0` (was `>=1.35` floating).

### Fixed

- `.github/CODEOWNERS` restored after deletion by b6d4fbc (PR #11).
- `.gitignore` now excludes Python bytecode (`__pycache__/`, `*.py[cod]`,
  `*.pyo`) to prevent accidental commit of generated artifacts (PR #15,
  closes audit finding L-1).
