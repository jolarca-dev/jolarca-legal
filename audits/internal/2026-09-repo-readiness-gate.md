# Internal audit — Repository readiness & first-commit gate

| Field | Value |
|-------|-------|
| Audit ID | `2026-09-repo-readiness-gate` |
| Scope | `jolarca-dev/jolarca-legal` — repository governance, access control, branch protection, secret hygiene, CI gate integrity |
| Date performed | 2026-09-28 |
| Auditor | Automated readiness audit (read-only Phase 1), operator-reviewed |
| Remediation owner | @JourneyOfLife (sole operator) |
| Verdict at audit | **BLOCKED** |
| Verdict after remediation | **READY-WITH-FIXES** (content) / **BLOCKED for launch** (B-2 open) |
| Close date | **PARTIAL** — B-1/B-3/B-4/H-1 CLOSED 2026-09-28; B-2 open on a billing decision |
| Compliance framing | SOC 2 Type II (CC6.1, CC6.6, CC7.1, CC8.1) · ISO 27001 (A.5.24, A.8.2, A.8.32, A.16.1) · GDPR Art. 7 |

Phrasing is non-privileged by design: this record describes **control**
failures only. It contains no client, dispute, counterparty, or personal
data, and may be forwarded to `jolarca-compliance/risk-register` as-is.

---

## 1. Why this audit exists

The repository was presented as newly created and awaiting a first commit.
That premise was **false**. Verification showed the repository was created
2026-08-14, carries 11 commits on `main`, 10 historical pull requests, live
nightly CI, and committed legal work product. The audit was therefore
re-scoped from "pre-first-commit gate" to "current-state control review",
which surfaced an **active regression on the default branch**.

---

## 2. Findings register

Severity: Blocker / High / Medium / Low.
Status values: **VERIFIED** = evidence observed; **ASSUMED** = not directly provable.

### 2.1 Corrections made to this audit during execution

Recorded deliberately. An audit that silently edits its own conclusions is
worthless; the correction trail is part of the evidence.

**Correction 1 — H-2 signature finding was materially overstated.**
The initial pass read `%G?` from a **local** `git log` and reported "10 of 11
commits unsigned or unverifiable", characterising 8 commits as signed with an
unregistered key `B5690EEEBB952194`. That was **wrong**. `B5690EEEBB952194` is
**GitHub's own** signing key, applied to commits GitHub creates (merge button,
Dependabot). Those commits report `verification.verified = true, reason =
valid` server-side; they show `E` locally only because GitHub's public key is
not in the auditor's keyring. Queried authoritatively, **9 of 11 commits are
verified** and only `9b72835` and `b6d4fbc` are truly unsigned. Severity
reduced High → Medium; scope re-written.

**Correction 2 — L-3 was a false finding, now retracted.**
"Nine stale remote branches" was derived from `git branch -r`, which lists
**local remote-tracking refs** that survive remote deletion until a `--prune`
fetch. The authoritative `gh api repos/.../branches` returns **`main` only**.
No stale branches exist. Finding retracted; no action required.

**Shared root cause of both errors — and the control lesson:** in each case a
**local cache was trusted over the authoritative remote source.** The same
class of error also produced the initial misreading of this repository's state
(a stale local `main`, 2 commits behind, hiding that CODEOWNERS had been
deleted upstream). Any future audit of this fleet must assert remote state
from the remote API, and local `%G?` must never be used as signature evidence
without confirming against `commit.verification`.

**Correction 3 — one checkpoint assertion was badly written.**
During R-3 the checkpoint `grep -c 'journeyoflife-org' .github/CODEOWNERS`
must equal `0` reported **FAIL** on a correct file: the single match is on a
**comment line** documenting decision D-20 (*"previous version referenced
@journeyoflife-org/*"*). The only active directive is `* @JourneyOfLife`. The
file was correct; the assertion failed to exclude comments. Recorded because a
checkpoint that produces false failures will eventually be ignored — and an
ignored checkpoint is worse than none.

### B-1 — CODEOWNERS deleted from default branch; required check RED *(Blocker)*

- **Status:** VERIFIED — **FIXED AND MERGED**
- **Evidence:** `b6d4fbc` (2026-09-25 20:02) deleted `.github/CODEOWNERS`
  (`1 file changed, 12 deletions`) while its message claimed to *enforce* it.
  Three minutes earlier `9b72835` — **identical commit message** — had
  correctly rewritten the file. Run `36164555365`, step *Governance files
  present*: `MISSING/EMPTY: .github/CODEOWNERS`. Check-rollup on
  `b6d4fbc`: `compliance = failure`, all others `success`.
- **Root cause:** duplicated-message deletion, characteristic of a stray
  `git rm` or a rebase/force-push artifact. Aggravating cause: **no branch
  protection existed to reject a direct push to `main`** (see B-2), and the
  failure went unnoticed for 3 days because **no audit covered CI-gate
  integrity** (see §4).
- **Corrective action:** restored `9b72835` content verbatim
  (`* @JourneyOfLife`) on `fix/restore-codeowners-b6d4fbc` → commit
  `77f0e30`, signed (`G`), 1 file / +12 / −0, PR #11.
- **Effectiveness verification (post-merge, Step F):** PR #11 merged
  2026-09-28T19:22:33Z by `JourneyOfLife`, squash commit `865518a`. On
  `origin/main`: `.github/CODEOWNERS` PRESENT (478 bytes, final line
  `* @JourneyOfLife`); check-rollup on default branch →
  `ci = success`, `compliance = success`, `security = success`.
  Local `main` fast-forwarded, `0 ahead / 0 behind`.
- **Settings confirmed unchanged by the fix:** `private: true`,
  `default_branch: main`, `archived: false`, deploy keys `0`, teams `0`.
- **Residual risk:** none for B-1 itself. **Recurrence risk is fully governed
  by B-2** — nothing prevents another direct push to `main` deleting this
  file again. B-1 is the symptom; B-2 is the disease.
- **CLOSED** 2026-09-28.

### B-2 — Branch protection and rulesets impossible on current plan *(Blocker)*

- **Status:** VERIFIED — **OPEN** (requires billing decision; operator action)
- **Evidence:** org `jolarca-dev` plan = `free`, repo `private`. Both
  `/branches/main/protection` and `/rulesets` return HTTP 403:
  *"Upgrade to GitHub Pro or make this repository public to enable this
  feature."* Corroborated by `b6d4fbc` / `9b72835` reaching `main` as direct
  pushes, and by `ci.yml:2` asserting *"branch protection requires the `ci`
  status check"* — describing a control that does not exist.
- **Impact:** mandated gates (PR required, ≥1 approval, force-push blocked,
  deletion blocked, required status checks) are **unenforceable**. Direct
  pushes to `main` are unimpeded; this is what allowed B-1 to land.
- **Decision recorded:** upgrade org to GitHub Team.
- **Constraint the operator must plan for:** with a **single-member org**,
  a "≥1 approval" rule **deadlocks every PR** — GitHub prohibits approving
  your own pull request. Configure the ruleset to require **status checks +
  block force-push + block deletion**, and either grant a documented
  admin bypass or accept 0 required approvals. Record whichever is chosen as
  an accepted risk. Do not discover this at merge time.
- **ASSUMED, not verified:** whether GitHub Team includes secret scanning /
  code scanning for **private** repos (historically an Advanced Security
  entitlement). **Confirm the entitlement matrix before purchase.**

### B-3 — Pre-commit hook executed a different repository's toolchain *(Blocker)*

- **Status:** VERIFIED — **FIXED**
- **Evidence:** `.git/hooks/pre-commit` contained
  `INSTALL_PYTHON=/opt/jolarca/repos/jolarca-infrastructure/.venv/bin/python`;
  that path existed and resolved `pre_commit` from the **infrastructure**
  repo's site-packages. `pre-commit` was absent from this repo's `.venv/bin`
  and from `PATH`.
- **Impact:** every commit was gated by tooling owned by another repository,
  at versions this repo's `pyproject.toml` does not pin. Non-reproducible
  change control (ISO 27001 A.8.32, SOC 2 CC8.1).
- **Corrective action:** installed `pre-commit 4.6.2` + `yamllint 1.38.0`
  into this repo's venv; `pre-commit install --install-hooks -f`.
- **Effectiveness verification:** hook now reads
  `INSTALL_PYTHON=/opt/jolarca/repos/jolarca-legal/.venv/bin/python`; commit
  `77f0e30` ran 8 hooks from the correct environment, all Passed/Skipped.

### B-4 — Virtual environment non-functional after repository relocation *(Blocker, local only)*

- **Status:** VERIFIED — **FIXED** (local; `.venv/` is gitignored, no repo impact)
- **Evidence:** `.venv/bin/pip` shebang was
  `#!/opt/jol-m/repos/jol-m-legal/.venv/bin/python` — a path that no longer
  exists. `pyvenv.cfg` recorded
  `command = ... -m virtualenv /opt/jol-m/repos/jol-m-legal/.venv`.
  Every console script failed with *"cannot execute: required file not found"*.
- **Root cause:** the repository was relocated `jol-m-legal → jolarca-legal`
  and `/opt/jol-m → /opt/jolarca` without rebuilding the venv. **This is the
  common root cause of B-3 and of the stale references in L-2.** The IDE
  interpreter was pointed at this broken environment.
- **Corrective action:** `python3 -m venv .venv` then
  `pip install --upgrade --force-reinstall pip` to regenerate console-script
  shebangs (avoids destroying site-packages).
- **Effectiveness verification:** `sys.prefix` =
  `/opt/jolarca/repos/jolarca-legal/.venv`; `pip --version` → pip 26.1.2;
  `pip` shebang now correct.

### H-1 — Local `main` diverged from origin with no upstream *(High)*

- **Status:** VERIFIED — **FIXED**
- **Evidence:** local `main` at `2791435` (2026-09-09) vs `origin/main` at
  `b6d4fbc` (2026-09-25); `0 ahead / 2 behind`;
  `git rev-parse main@{upstream}` → *fatal: no upstream configured*.
- **Landmine:** the working tree held the **stale, wrong-org** CODEOWNERS, so
  the defect was invisible locally. A plain `git pull` deletes the file and
  *looks* like data loss.
- **Corrective action:** created rollback anchor `backup/pre-sync-2026-09-28`;
  `git branch --set-upstream-to=origin/main main`; `git merge --ff-only`.
- **Effectiveness verification:** `main == b6d4fbc`, `0 ahead / 0 behind`,
  worktree clean, upstream set.

### H-2 — Two commits unsigned; no signing gate on direct pushes *(Medium — severity CORRECTED, see §2.1)*

- **Status:** VERIFIED — **CORRECTED; residual gap OPEN, forward-looking fix in place**
- **Authoritative evidence** (GitHub `commits/{sha}` → `commit.verification`,
  which is server-side and does not depend on the auditor's local keyring):

  | Commit | `verified` | `reason` |
  |--------|-----------|----------|
  | `865518a` (PR #11 merge) | **true** | valid |
  | `2791435` | **true** | valid |
  | `e15464a` | **true** | valid |
  | `00ec32e` | **true** | valid |
  | `5bcd0d8` | **true** | valid |
  | `9b72835` | **false** | **unsigned** |
  | `b6d4fbc` | **false** | **unsigned** |

- **Actual scope of the defect:** **9 of 11 commits are GitHub-verified.**
  Only **`9b72835` and `b6d4fbc` are genuinely unsigned** — and those are
  *precisely the two direct local pushes to `main` that caused B-1*.
- **Corrected root-cause reading:** one failure mode, two symptoms. Both
  rogue commits were local pushes that reached `main` unguarded because B-2
  leaves it unprotected, and both bypassed signing. The signing gap and the
  CODEOWNERS deletion are the same governance failure, not two.
- **Impact (re-scoped):** non-repudiation is absent for the two commits that
  made an unreviewed change to the legal record's governance (SOC 2
  CC6.1/CC6.6, ISO 27001 A.8.2). Narrower than first reported, but it lands
  exactly on the highest-risk change in the repository's history.
- **Corrective action:** local config confirmed correct
  (`user.signingkey=<configured>`, `commit.gpgsign=true`). Commit
  `77f0e30` was created with `-S` and verifies locally as **`G` — JOL
  Platform Signing Key**; its squash-merge descendant `865518a` verifies
  **`true/valid`** on GitHub.
- **Not remediated:** the two unsigned commits remain unsigned. Rewriting
  published history to re-sign them is **not recommended** — it would destroy
  more audit integrity than it restores. Record as an accepted limitation
  with the effective date of the signing fix, and rely on B-2 remediation to
  prevent recurrence.
- **Structural note:** GitHub-created commits (merge button, Dependabot) are
  signed with **GitHub's** key, not the operator's. Those verify as `valid`
  on GitHub but may show `E` locally with *"Can't check signature: No public
  key"*. **`E` in a local `git log` is not evidence of a bad signature** —
  always confirm against `commit.verification.verified`. See §2.1.

### H-3 — Test suite never executed by CI *(High)*

- **Status:** VERIFIED — **OPEN**
- **Evidence:** `scripts/tests/test_check_csv.py` contains 5 regression tests;
  executed locally → `Ran 5 tests in 0.113s / OK`. But
  `grep -rn 'pytest|unittest' .github/workflows/` → **no test invocation in
  any workflow**. `ci.yml` runs yamllint, three validators, shellcheck only.
- **Impact:** the readiness requirement of lint **+ tests** is unmet; the one
  component with automated coverage is ungated.
- **Corrective action (pending):** add to `ci.yml` after *Personal-data
  pattern scan*:
  `- name: Unit tests (scripts)` / `run: python3 -m unittest discover -s scripts/tests -v`.
  Safe: stdlib-only, zero new dependencies, already green.

### M-1 — ADR-0004 and ADR-0003 cited but absent; ADR gate passes vacuously *(Medium)*

- **Status:** VERIFIED — **OPEN, requires operator/GC decision**
- **Evidence:** `b6d4fbc` / `9b72835` cite *"ADR-0004 R4"*, *"D-20"*, *"D-10"*.
  `.sops.yaml:1` cites *"ADR-003 amendment PR #35"*;
  `secrets/encrypted/README.md:1` cites *"ADR-003 amendment, R3 convention"*.
  `docs/adr/` contains only `0001-...md` + `README.md`.
- **Impact:** the rationale used to justify deleting CODEOWNERS is evidenced
  nowhere in this repository (ISO 27001 A.5.36 traceability).
- **Compounding defect:** the *ADR numbering continuous* gate is
  `awk 'NR>1 && $1!=p+1'` — with a single numbered file `NR>1` never
  evaluates, so **the gate cannot fail**. A control that only fires when ≥2
  ADRs exist is not a control.
- **Deliberate non-action:** the auditor **did not author ADR-0003/0004**.
  Those record decisions the auditor did not make; writing plausible ADRs to
  close an evidence gap would fabricate compliance records and convert a
  documentation gap into a fraud finding. **Operator/GC must author or
  cross-reference them.**

### M-2 — Supply-chain pinning inconsistency *(Medium)*

- **Status:** VERIFIED — **OPEN**
- **Evidence:** 9 of 10 `uses:` directives are SHA-pinned. Exception:
  `security.yml:17` → `actions/checkout@v7` (tag). Repo settings:
  `allowed_actions: "all"`, `sha_pinning_required: false`.
- **Corrective action (pending):** pin to
  `3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1`, matching every other
  workflow. Set `sha_pinning_required: true` **only after** the pin lands.

### M-3 — Floating unpinned dependency in CI *(Medium)*

- **Status:** VERIFIED — **OPEN**
- **Evidence:** `ci.yml:23` → `pip install --quiet "yamllint>=1.35"`.
- **Impact:** a future upstream release can change gate behaviour with no
  repository change — non-reproducible builds (SOC 2 CC8.1).
- **Corrective action (pending):** pin exact (`yamllint==<verified current>`).

### M-4 — Consent re-evaluation control is a permanent no-op *(Medium)*

- **Status:** VERIFIED — **OPEN, enter in risk register**
- **Evidence:** `legal-text-sync.yml` advertises notifying the consent
  registry so that *"consent recorded against an old version must be
  re-evaluated"*. But repository secrets = **none configured**, so
  `COMPLIANCE_RO_TOKEN` resolves empty; and `cross-check-consent.py` returns
  **`0` on both branches** — offline mode (L59) and the token-present stub
  (L61-65: *"intentionally stays a stub until that contract exists"*).
- **Impact:** the control **always exits 0 and never contacts a registry**.
  It is honestly documented as a stub — hence Medium, not High — but a green
  check that proves nothing is how GDPR Art. 7 re-consent obligations get
  missed. **Must be recorded as a non-operational control**, not treated as
  coverage because CI is green.

### M-5 — Issues disabled; pipeline "linked issue" step impossible *(Medium)*

- **Status:** VERIFIED — **OPEN (documentation fix)**
- **Evidence:** `has_issues: false`, `has_projects: false`,
  `has_discussions: false`. PRs function normally.
- **Corrective action:** reword the commit pipeline to require a linked
  **audit finding ID / PR context** instead of an issue.

### L-1 — Python bytecode not gitignored *(Low)*

- **Status:** VERIFIED — **OPEN**
- **Evidence:** `.gitignore` covers `.venv/`, `*.pem`, `*.key`, `.env` etc.
  but **not** `__pycache__/` or `*.py[cod]`. Running the test suite produced
  an untracked `scripts/tests/__pycache__/`.
- **Note:** the artifact created during this audit was deleted and its
  removal re-verified (no `.pyc` remained).

### L-2 — Stale rename debt *(Low)*

- **Status:** VERIFIED — **OPEN**
- **Evidence:** `.sops.yaml` references `/opt/jol-m/**` and
  `jol-infrastructure`; `secrets/encrypted/README.md:6` references
  `jol-infrastructure`; `legal-text-sync.yml:43` targets
  `journeyoflife-org/jolarca`.
- **Root cause:** same incomplete `jol-m → jolarca` relocation as B-4.
- **Caution:** `.sops.yaml` carries key-custody semantics (age recipient,
  tree segregation). Sweep the **prose** references, but review the
  `path_regex` / recipient rules with the key custodian before editing.

### L-3 — ~~Nine stale remote branches~~ **RETRACTED — false finding** *(None)*

- **Status:** **RETRACTED.** The original evidence was wrong.
- **What was reported:** `git branch -r` listed 9 non-`main` remote branches
  (`compliance/step26-vmi-isaf-record`, 4× `dependabot/*`,
  `feat/add-security-workflow`, `feat/complete-legal-pack`,
  `feat/initial-content`, `security/sops-enablement`).
- **Why it was wrong:** `git branch -r` reads **local remote-tracking refs**,
  which persist after the remote branch is deleted until a `--prune` fetch
  removes them. The authoritative query
  `gh api repos/jolarca-dev/jolarca-legal/branches` returns **`main` only**.
  Those branches were already deleted on GitHub (head-branch auto-delete
  after each merge); only the auditor's local refs were stale.
- **Lesson recorded:** never report remote repository state from local
  remote-tracking refs. Query the remote. This is the same class of error as
  the H-2 signature misreading — **trusting a local cache over the
  authoritative source.**
- **No action required.**

---

## 3. Controls that PASSED — retained as positive evidence

| Control | Evidence |
|---------|----------|
| No secrets in repository or history | gitleaks 8.30.1 full-history: 20 commits / 736 KB → `no leaks found`, exit 0. Independently corroborated by green nightly `security` workflow on `main` |
| No ciphertext committed | `secrets/encrypted/` holds only `README.md`; SOPS recipient is a **public** age key |
| Least-privilege Actions tokens | every workflow declares `permissions: contents: read` |
| Access control | 0 teams, 0 deploy keys, 1 collaborator (owner); `members?filter=2fa_disabled` empty; `two_factor_authentication: true` |
| Dependabot | config present (actions weekly, pip monthly); alerts enabled (`204`); 0 open alerts |
| License | proprietary — *"All rights reserved"*, *"PRIVATE"*, *"INTERNAL USE ONLY"*; **not** AGPL |
| Validators | `legal-text-version.py --validate`, `renewal-report.py --check-register`, `check-personal-data.sh` → all exit 0 |
| Visibility | `private` — correct for privileged legal material |

---

## 4. Systemic observation — audit programme blind spot

The five audits defined in `audits/README.md` cover **access review, register
integrity, legal-text sync, retention sweep, renewal windows**.

**None covers governance-file integrity or CI-gate health** — which is
precisely the control that silently broke and stayed broken for three days.
The audit programme had a blind spot exactly where the failure occurred.

**Recommendation:** add a cadence row —
`| Governance & CI integrity | monthly | required checks green on default branch; all gated governance files present and non-empty; pre-commit hook resolves inside this repository; commits signed and verifiable |`

A second systemic point: B-1, B-4 and L-2 share **one root cause** — an
incomplete `jol-m → jolarca` relocation. Fixes applied file-by-file will
leave siblings behind. The relocation should be swept once, deliberately.

---

## 5. Remediation status summary

| ID | Severity | Status | Verified by |
|----|----------|--------|-------------|
| B-1 | Blocker | **FIXED** — PR #11, all checks green | `compliance` pass; `mergeStateStatus: CLEAN` |
| B-2 | Blocker | **OPEN** — operator billing decision | two independent HTTP 403s |
| B-3 | Blocker | **FIXED** | hook `INSTALL_PYTHON` path; 8 hooks ran clean |
| B-4 | Blocker | **FIXED** (local) | `sys.prefix`; `pip --version` |
| H-1 | High | **FIXED** | `0 ahead / 0 behind`, upstream set |
| H-2 | Medium *(was High)* | **CORRECTED & PARTIAL** — 9/11 GitHub-verified; only `9b72835`/`b6d4fbc` unsigned | `commit.verification.verified` per SHA |
| H-3 | High | **OPEN** | no test invocation in any workflow |
| M-1 | Medium | **OPEN** — operator/GC must author | `docs/adr/` listing |
| M-2 | Medium | **OPEN** | pinning grep |
| M-3 | Medium | **OPEN** | `ci.yml:23` |
| M-4 | Medium | **OPEN** — risk-register entry required | `cross-check-consent.py` both branches return 0 |
| M-5 | Medium | **OPEN** | `has_issues: false` |
| L-1 | Low | **OPEN** | `.gitignore` contents |
| L-2 | Low | **OPEN** | stale-reference grep |
| L-3 | — | **RETRACTED** — false finding, stale local refs | `gh api .../branches` → `main` only |

**Overall verdict: BLOCKED — downgraded to READY-WITH-FIXES for the
repository content, still BLOCKED for launch.**

B-1 is **fixed, merged, and verified green on `main`**. B-3, B-4 and H-1 are
fixed and verified. B-2 **cannot be remediated without an operator billing
decision**, and until it is, nothing prevents a repeat of B-1 — a direct push
to `main` can still delete any governance file, unsigned, with no review and
no protection.

**Open items:** B-2 (operator), H-2 residual (accepted limitation), H-3, M-1
(operator/GC), M-2, M-3, M-4 (risk register), M-5, L-1, L-2. **Retracted:**
L-3.

---

## 6. Sign-off

> I have read findings B-1 through L-3 in full. I understand this
> repository's verdict is **BLOCKED**, that a required check failed on the
> default branch for three days, that **branch protection cannot be enforced
> on the current plan**, and that my local toolchain was validating against
> another repository's environment. I will not commit, push, or merge until
> the blocker checkpoints pass. I will not use `--no-verify`. I will not push
> to `main`.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Auditor | (automated readiness audit) | — | 2026-09-28 |
| Operator / remediation owner | | | |
| Reviewer (General Counsel) | | | |
