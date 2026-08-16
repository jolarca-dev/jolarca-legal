# Architecture — jol-m-legal in the fleet

Template-inherited baseline, extended for the legal function: how legal
texts flow into product builds, and where each legal artifact's custody
lives.

## Repository boundaries

```
jol-m-legal            legal instruments, texts, governance (this repo)
  │  publishes tagged legal-text versions (legal-text-sync.yml)
  ▼
jol-m-marketplace      product code; PINS legal-text versions
  │  consent records reference text versions
  ▼
jol-m-compliance       RoPA, lawful-basis registry, DPIA records,
                       risk register, DSAR logs (GDPR evidence home)

jol-m-infrastructure   runs the planes; no legal content
```

Rules:

- **Single canonical source.** Marketplace-facing texts exist once:
  `legal-texts/`. The product consumes pinned versions; it never edits.
- **Evidence segregation.** GDPR operational evidence lives in
  `jol-m-compliance`; this repo holds instruments + analysis. Cross-refs
  are by path/id, never by copying content.
- **Privilege boundary.** Nothing privileged crosses repository
  boundaries — not even summaries. Matter ids travel; substance does not.

## The legal-text flow (detail)

1. Draft in `legal-texts/<text>/<lang>/` with front-matter (`status:
   draft`), reviewed in PR with GC as CODEOWNER.
2. Approval: `status: approved`, `effective_date` set; CHANGELOG.md gets
   the plain-language entry. MAJOR bumps additionally need P2B notice
   evidence (`platform-regulation/p2b/tos-change-notice.md`).
3. Tag `legal-texts-vX.Y.Z` → `legal-text-sync.yml` builds the publish
   manifest (`scripts/legal-text-version.py --manifest`), cross-checks
   the consent registry (`scripts/cross-check-consent.py`), and opens
   the marketplace PR pinning versions.
4. Product build reads pinned versions; consent UI shows the text
   version recorded at consent time.

## Custody model

| Artifact | Git role | Custody of original |
|----------|----------|---------------------|
| Executed contracts | metadata + negotiated text | DMS (signed original) |
| Corporate filings | text extract / pointer | register/notary originals |
| Insurance policies | schedule summaries | DMS (wording PDFs) |
| Evidence | index pointers only | DMS |

Git is the index and the text of record; signed binaries live in the DMS,
with `.gitattributes` keeping binaries out of textual diffs.
