# Changelog — jol-m-legal

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
