# employment/ — Employment & contractor agreements (ACCESS-RESTRICTED)

Executed employment contracts and contractor agreements. This path has the
tightest non-privileged restriction in the repository:

- CODEOWNERS: GC only. No reviews from outside the access list.
- Names appear only where the instrument requires them; compensation,
  bank details, and national IDs are NEVER committed — they live in the
  sealed HR custody location referenced by `metadata.md`.
- Contractor agreements file here (not under `vendors/`) when the
  relationship is personal-services work product; IP assignment CL-40
  is mandatory in the instrument.

Templates: `00-templates/employment-template.md` (LT labor code compliant)
and `00-templates/contractor-agreement.md`.

Register: employment instruments are tracked in a private register kept in
the HR custody location (not git), with only status/date columns mirrored
here if automation requires it.
