# Project creation

```bash
% uv init rgs-project  # Create a project
% cd rgs-project

% uv run rgs-project   # Run the project command (see pyproject.toml > [project.scripts])

% uv add rich          # Add the dependency `rich`
```

- uv installation instructions: https://docs.astral.sh/uv/getting-started/installation/
- uv project management: https://docs.astral.sh/uv/guides/projects/
- uv dependency management: https://docs.astral.sh/uv/concepts/projects/dependencies/

1. Set up your own project.
2. Add some source code.
3. Add a dependency.
4. Check that everything runs.
5. Create a GitHub repository for your project and commit everything


# Quality checks

```bash
% uv add --dev ty ruff     # Add development dependencies

% uv run ruff format       # Format code
% uv run ruff check        # Lint your code
% uv run ruff check --fix  # Lint and auto-fix your code
% uv run ty check          # Type-check your code
```

- uv dependency management: https://docs.astral.sh/uv/concepts/projects/dependencies/
- uv tool running: https://docs.astral.sh/uv/concepts/projects/run/
- Ruff documentation: https://docs.astral.sh/ruff
  - Formatting: https://docs.astral.sh/ruff/formatter/
  - Linting: https://docs.astral.sh/ruff/linter/
- ty documentation: https://docs.astral.sh/ty/

1. Mess up the format of your code on purpose.
2. Add unused imports.
3. Change the type hints so they become wrong.
4. Install Ruff and ty as development dependencies.
5. Run a formatter, a linter, and a type checker.
6. Fix all issues you find along the way.
7. Take your project and upload it to a GH repo.


# Testing

Tests live in `<project root>/tests`.

```bash
% uv add --dev pytest  # Add development dependency for testing
% uv run pytest        # Run the tests
```

- pytest documentation: https://docs.pytest.org/en/stable/

1. Create your own folder for tests.
2. Add different testing scenarios.
3. Parametrize one of your tests.
4. Purposely break your code.
5. Check that the tests fail.
6. Fix your code.
7. Check that the tests pass.


# Automatic quality checks on commit

Pre-commit configuration lives in `.pre-commit-config.yaml`.

```bash
% uv add --dev pre-commit                                    # Add dev dependency for pre-commit hooks

% uv run pre-commit sample-config > .pre-commit-config.yaml  # Create sample configuration file

% # Configure remaining hooks...

% uv run pre-commit install                                  # Install the hooks

% uv run pre-commit run --all-files                          # Sanity check: run all hooks
```

- pre-commit documentation: https://pre-commit.com/#install
- Ruff pre-commit: https://docs.astral.sh/ruff/integrations/#pre-commit

1. Set-up pre-commit.
2. Add hooks for all the tools that we're running.
3. Add a local hook to run pytest.
4. Try to make a commit with a problem (e.g., formatting is off).
5. Check that the commit is blocked.

---

# BREAK

1. Create an account on https://test.pypi.org
2. Verify your email address
3. Enable 2-Factor Authentication (2FA) for your account
4. Make sure that the project you're working on is pushed to a public GitHub repo

---
