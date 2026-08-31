# Contributing — jolarca-legal

Legal operators and counsel. Every merge here is a legal record; the
history must stand up as evidence. Commits follow Conventional Commits;
every term change is auditable through `CHANGELOG.md`.

## Versioning doctrine

1. **Redlines are preserved.** Negotiation history lives in the branch/PR
   history and in `*-redline-*` artifacts inside the instrument folder.
   Never squash-away negotiation steps on executed instruments — merge
   with full history visible to GC.
2. **Executed versions are immutable.** Once an instrument is marked
   `executed` (folder move + register status), its content changes only
   via amendment or restatement — a new document referencing the
   original. Never edit an executed text "in place".
3. **Legal texts are SemVer'd, one version per text** (`legal-texts/`):
   - MAJOR — material term change (P2B: 30-day notice + evidence archive);
   - MINOR — new clauses/sections that change rights or obligations;
   - PATCH — clarifications, typos, formatting, no change of meaning.
   The product pins a version; published versions are never rewritten.
4. **Plain-language change logs.** Every legal-text version carries a
   plain-language summary in its `CHANGELOG.md` — this is our DSA/P2B
   notice evidence, not a developer nicety.

## Workflow

1. **Issue first.** Use the matching intake template
   (`contract_request`, `legal_review_request`, `regulatory_change`).
2. **Branch per instrument/matter.** One concern per PR.
3. **CI is a merge gate.** `ci` and `compliance-check` must be green:
   front-matter validation, register consistency, governance files.
4. **CODEOWNERS routing is binding.** GC review on `legal-texts/` and
   `contracts/`; privileged paths are restricted — do not open them for
   unrelated reviews.

**Solo-era operation (current):** the org operates with a single legal
operator, so human review gates ride on automated checks + CODEOWNERS
routing until counsel/second operator onboards. This is a tracked
deviation, not an exemption: the routing stays in place and activates.

## Personal data — minimization is mandatory

**Privilege ≠ PII-free.** Privileged documents routinely contain personal
data; GDPR applies inside this repository.

- Commit personal data only when load-bearing (named signatory, officer,
  counterparty contact) and never more than name/title/email needed.
- No national IDs (asmens kodas / personas kods / isikukood), no health,
  no bank details in markdown; reference the custody location instead
  (e-signature envelope, HR system, register extract).
- `employment/` is access-restricted: names appear only where the
  instrument requires them; compensation goes in the sealed envelope, not
  in git-tracked markdown.
- The pre-commit personal-data pattern scan (`scripts/check-personal-data.sh`)
  is a tripwire, not a license: passing it does not make a commit lawful.

## Secrets & custody

- No tokens, keys, or credentials — gitleaks enforces.
- Signed originals: the git record is the metadata + pointer; signed PDFs
  live in the document-management custody location. Local signed-PDF
  caches and e-signature envelope exports are gitignored by design.
- Apostilles/notarizations: scanned certificates are filed under
  `corporate/registrations/` with the filing reference in the filename.

## Change-risk classes

| Class | Examples | Gate |
|-------|----------|------|
| Low | Docs, reserved scaffolding, indexes | 1 review |
| Med | Memos, templates, clause library drafts | 1 review (GC) |
| High | Legal-text term changes, contract templates | GC review + version bump + changelog |
| Crit | Executed instrument handling, privilege material, publication tags | GC + counsel; publication via pipeline only |

If you cannot describe who may see the material and how it is reverted,
the change is not ready.
