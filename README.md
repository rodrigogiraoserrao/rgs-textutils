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

# GitHub Actions

GH Action configuration lives in `.github/workflows/*.yaml`.

- GitHub Actions quickstart: https://docs.github.com/en/actions/get-started/quickstart
- uv GitHub action: https://docs.astral.sh/uv//guides/integration/github/

1. Set up your GH repo
2. Set up the code-quality.yaml workflow
3. Run it (manually or by opening a PR)
4. Complete the action so it also runs linting, type checking, and the tests
5. Trigger it again to make sure it works


# Publishing to (Test)PyPI

If you save your token in `.env`, make sure to add that file to `.gitignore`!

```bash
% uv build                                                # Build the project

% # Add the TestPyPI configuration to pyproject.toml.

% uv publish --index testpypi --token <paste token here>  # Publish to Test PyPI

% set -a; source .env; set +a                             # Export the UV_PUBLISH_TOKEN in .env (Unix/WSL)
% uv publish --index testpypi                             # Publish to Test PyPI using the token from .env
```

- Test PyPI: https://test.pypi.org/
- uv package publishing documentation: https://docs.astral.sh/uv//guides/package/


# Trusted publishing

```bash
% uv version --bump major      # Bump major version
% uv version --bump minor      # Bump minor version
% uv version --bump patch      # Bump patch version

% git tag -a vX.Y.Z -m vX.Y.Z  # Create the tag vX.Y.Z

% git push                     # Push changes and tags
% git push --tags              # Push just the tags
```

- uv trusted publishing documentation: https://docs.astral.sh/uv//guides/integration/github/#publishing-to-pypi

1. Create the `release.yaml` workflow
2. Create the `testpypi` environment on GitHub (under settings)
3. Set up trusted publishing from the Test PyPI account
4. Create a new tag and push it to test everything
