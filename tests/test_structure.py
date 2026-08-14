"""Smoke tests for the jol-m-legal repository scaffold."""


def test_template_structure() -> None:
    """Verify that essential repository files exist."""
    from pathlib import Path

    root = Path(__file__).resolve().parent.parent
    required = [
        "README.md",
        "LICENSE",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "pyproject.toml",
        "Makefile",
        ".editorconfig",
        ".gitignore",
    ]
    for filename in required:
        assert (root / filename).is_file(), f"Missing required file: {filename}"
