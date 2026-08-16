# ADR-0001: Legal texts as versioned build artifacts, not CMS content

**Status:** accepted · **Date:** 2026-08-15 · **Decider:** GC

## Context

Marketplace legal texts (ToS, privacy, seller agreement, buyer terms…)
must be: reviewable by counsel, translatable to LT/LV/ET, provable as
notified (P2B/DSA), pinned by the product, and auditable per version.
A CMS/marketing-content model fails these: history is mutable, review
gates are informal, and publication is decoupled from the product build.

## Decision

Legal texts live in `jol-m-legal/legal-texts/` as markdown with SemVer
front-matter. The product (`jol-m-marketplace`) pins a version; tags
(`legal-texts-vX.Y.Z`) drive a publication pipeline that validates,
cross-checks consent records, and opens the pinning PR. Published
versions are immutable; changes ship as new versions with plain-language
changelogs (our notice evidence).

## Consequences

- Every legal-text change is a code-style PR with GC review — slower
  than CMS editing, deliberately.
- Consent registry must record text versions (cross-check script).
- Translations are first-class files with the same version number as
  their source.
- Rejected alternatives: CMS with export pipeline (mutable history,
  weak review gates); PDF-only custody (no diffing, no machine
  validation).
