# corporate/ — Corporate governance records

Entity: **UAB "Journey of Life"** (Lithuania). This tree is the corporate
record of the entity: formation, board activity, ownership, signing
authority, and statutory registrations.

## Structure

| Path | Contents |
|------|----------|
| `formation/` | Incorporation docs, articles of association, register extracts |
| `board/` | Minutes & resolutions — one numbered folder per meeting |
| `cap-table/` | Shareholder register, option grants (if any) |
| `powers-of-attorney/` | Who may sign what; revocation log |
| `registrations/` | VAT (LT), OSS, EORI, LEI, business-register filings |

## Conventions

- **Filenames carry dates:** `YYYY-MM-DD-subject.md` (or the registered
  document's own reference number where one exists).
- **Board meetings:** `board/YYYY-NN-short-title/` with `minutes.md` and
  one file per resolution (`resolution-01-*.md`). Resolutions cite the
  authority they rely on (articles clause / PoA).
- **Originals custody:** signed/apostilled/notarized originals live in the
  document-management custody location; git stores the text extract or a
  pointer + filing reference. Scans of apostille certificates file under
  `registrations/`.
- **Signing authority:** the live matrix is
  [`docs/signing-authority-matrix.md`](../docs/signing-authority-matrix.md);
  `powers-of-attorney/` holds the underlying instruments and the
  revocation log. Every PoA change updates both the same day.
- **Registrations:** one folder per regime; each entry records the filing
  date, authority reference, renewal obligation (if any), and the person
  responsible.

Changes to this tree are High-risk class (CONTRIBUTING.md): GC review,
no in-place edits of filed records — corrections land as new filings.
