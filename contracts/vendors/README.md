# vendors/ — Executed vendor contracts

One folder per vendor; every executed instrument has a row in
`_register.csv` (schema fixed — see header). Renewal automation
(`contract-renewals.yml`) parses the register weekly.

Expected vendors (folders created as instruments execute):

| Vendor | What runs through it |
|--------|----------------------|
| `stripe/` | Connected Account Agreement, platform terms, fee schedule |
| `google-cloud/` | Cloud services (ties to jol-m-compliance vendor assessment) |
| `deepl/` | Translation API |
| `openai/` | LLM services |
| `anthropic/` | LLM services |
| `dpd/` | Parcel delivery (LT/LV/EE) |
| `omniva/` | Parcel delivery (LV/EE) |
| `bitrix24/` | Internal tooling |

Folder convention: `metadata.md` (status, custody pointer) + dated
instrument files. Register row lands the day the instrument executes.
