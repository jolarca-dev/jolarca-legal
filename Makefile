# jol-m-legal — legal operator hygiene targets.
# Targets must stay runnable without credentials (pure-repo checks).

SHELL := /bin/bash
PY := python3

.PHONY: help check lint-docs versions renewal-report

help: ## Show targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  %-15s %s\n", $$1, $$2}'

check: ## Gate = front-matter + registers + personal-data scan (mirrors CI)
	$(PY) scripts/legal-text-version.py --validate
	$(PY) scripts/renewal-report.py --check-register
	bash scripts/check-personal-data.sh

lint-docs: ## Markdown/YAML hygiene for docs and workflows
	@command -v yamllint >/dev/null && yamllint .github/ .pre-commit-config.yaml qodana.yaml \
		|| echo "yamllint not installed — skipped"
	@command -v markdownlint >/dev/null && markdownlint '**/*.md' \
		|| echo "markdownlint not installed — skipped"

versions: ## Build the legal-text publish manifest (what ships to product)
	$(PY) scripts/legal-text-version.py --manifest

renewal-report: ## Upcoming renewals & notice windows from contracts register
	$(PY) scripts/renewal-report.py
