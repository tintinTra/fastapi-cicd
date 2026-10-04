## FastAPI CI/CD

Learning project for FastAPI and CI/CD 

## Goal 

implementing a FastAPI Server and pushing it trouh a CI/CD pipeline

## FastAPI server function: 
archiving e-books and saving it in a database
# Routing
- contains 1 get endpoint for status 
- contains 2 post endpoints for sending information for one book and for a list of books


## Formatting and linting with Ruff

The configuration is defined in `pyproject.toml`. Ruff formats code
consistently and checks for issues such as unused imports, undefined
names, and unsorted imports.

# Format
- all braces need to be double braces
- tabs need to be 4 spaces
- line endings are automatic depending on the os in linux lf and on windows ctrl-lf


Install dependencies from the lockfile:

```bash
uv sync --locked
```

During development, fix automatically correctable lint issues,
then format the code:

```bash
uv run ruff check --fix .
uv run ruff format .
```

Any remaining lint issues must be fixed manually.

Before committing and later in CI, run checks without modifying files:

```bash
uv run ruff check .
uv run ruff format --check .
```

These checks do not modify files. If they detect violations, they return
a nonzero exit code, causing the CI step to fail.

## API tests and CI

Install dependencies and run the tests locally:

```bash
uv sync --locked
uv run pytest -v
```

The tests in `tests/test_api.py` use FastAPI's `TestClient`, so no running
Uvicorn server is needed. They check the status endpoint, creating one or
multiple books, and rejecting invalid requests with HTTP 422 without
saving any books. A pytest fixture gives each test a fresh in-memory
dictionary so tests cannot affect each other.

The application currently stores data only in memory; these tests do not
exercise a persistent database.

GitHub Actions reads `.github/workflows/ci.yml`. On every push and pull
request, the workflow installs the locked dependencies, checks Ruff lint
and formatting, and runs `uv run pytest -v`. A failed assertion causes
pytest to exit with an error and the CI job to fail.

# Docker
Pushing it into a docker image
