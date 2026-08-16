# QODER.md

Behavioral guidelines to reduce common LLM coding mistakes when using Qoder in PyCharm. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.
- Prefer PyCharm's built-in refactoring tools (Rename, Extract Method, Move, etc.) over manual text manipulation when the IDE can do it safely.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

---

## Project-Specific Guidelines — jol-m-legal

This repository is the legal record of the organization; every merge must
stand up as evidence. The full rules live in `CONTRIBUTING.md`; these
constrain AI-assisted changes:

### Legal-text boundaries

- Never generate final legal wording for publication. Drafts are
  structural scaffolds; substantive terms are counsel-approved.
- Never rewrite a published legal-text version — new content lands as a
  new SemVer version with a plain-language CHANGELOG entry.
- Bump discipline: MAJOR = material term change (P2B 30-day notice),
  MINOR = rights/obligations change, PATCH = no change of meaning.
- Keep front-matter complete and valid (`version`, `status`,
  `effective_date`, `language`); `scripts/legal-text-version.py --validate`
  must pass.

### Privilege & confidentiality

- Treat `disputes/`, `regulatory/inquiries/`, and privileged memos as
  read-only context. Never summarize, quote, or paraphrase privileged
  material into other paths, repos, commits messages, or chat artifacts.
- Never propose moving privileged content "for convenience".
- Executed instruments are immutable: amendments are new documents,
  never in-place edits.

### Personal data

- Never invent or commit personal data. Names only where load-bearing
  (signatory, officer); never national IDs, bank details, health data.
- If a task seems to require personal data, stop and name the
  minimization problem.

### Automation gates

- `make check` (front-matter validation, register consistency, PII
  tripwire) must pass before proposing a change as complete.
- Never suggest bypassing pre-commit (`--no-verify`).
- Register changes (`contracts/**/_register.csv`) must keep schema
  intact; renewal automation parses them.
