# jol-m-legal

**PRIVATE repository.** Single source of truth for legal governance of the
Journey Of Life marketplace platform (LT / LV / EE markets): contracts,
platform terms, privacy-facing legal texts, and data processing agreements.

> Hard rule: this repository stores **legal governance artifacts only** —
> versioned texts, registers, and review tooling. It must **never** contain
> executed contracts with personal data of signatories, case files, or
> privileged correspondence; those remain in the legal matter management
> system. Here we keep texts, indexes, and references.

## Access

| Role | Access | Notes |
|---|---|---|
| Legal counsel | Admin | Required reviewer on all legal texts |
| DPO | Admin | Required reviewer on privacy-facing texts |
| Engineering leads | Write | Via PR only; branch protection enforced |
| Everyone else | None | Requests via issue, SLA: 2 business days |

## Structure

| Path | Content |
|---|---|
| `src/jol_m_legal/` | Legal tooling (text integrity checks, version diffing) |
| `tests/` | Scaffold and tooling tests |
| `docs/` | Architecture notes, DPIA template references |
| `.github/` | CI workflows, CODEOWNERS, issue/PR templates |

## Quick Start

```bash
# Clone the repository
git clone https://github.com/journeyoflife-org/jol-m-legal.git
cd jol-m-legal

# Create and activate a Python virtual environment (Python >= 3.12)
python3 -m venv .venv
source .venv/bin/activate

# Install development dependencies
make install-dev
```

## Compliance Baseline

| Standard       | Scope                                       |
|----------------|---------------------------------------------|
| GDPR           | Data processing, DPIA, cross-border transfer |
| ISO 27001      | Information security management              |
| SOC 2          | Trust service criteria                       |

All pull requests are subject to CODEOWNERS review. Security-sensitive paths
require additional approvers as defined in `.github/CODEOWNERS`.

## Workflows

| Workflow             | Trigger                         | Purpose                                      |
|----------------------|---------------------------------|----------------------------------------------|
| `ci.yml`             | Push to `main`, pull requests   | Lint, test, build validation                 |
| `compliance-check.yml` | Pull requests                 | License header and policy enforcement        |
| `codeql.yml`         | Push to `main`, pull requests   | Static analysis and vulnerability scanning   |

## Development

```bash
# Run linting
make lint

# Run tests
make test

# Run full pre-commit suite
make check
```

## Security

See [SECURITY.md](SECURITY.md) for the vulnerability disclosure process and security policy.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and the development workflow.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
