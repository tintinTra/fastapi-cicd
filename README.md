# FastAPI CI/CD

- Learning project for building a FastAPI REST API and setting up a CI/CD pipeline.
- Manages book metadata (title, ISBN, author); data is stored in memory and lost on restart.
- Current automation covers CI checks; a persistent database, Docker image, and automated deployment are planned.

## Application code — `src/fastapi_cicd/__init__.py`

- `main()`: starts Uvicorn at `127.0.0.1:8000` with automatic reload during development.
- `Book`: validates the title, ISBN, and author fields with Pydantic; author names require at least five characters.
- `db`: stores books in a dictionary keyed by ISBN; saving the same ISBN replaces the existing entry.
- `status()` — `GET /status`: returns `{"status": 200}` to check that the API responds.
- `get_books()` — `GET /books`: returns all stored books as JSON.
- `post_book()` — `POST /book`: validates, stores, and returns a single book.
- `multiple_books()` — `POST /books`: validates, stores, and returns a list of books.
- `get_book()` — `GET /book`: placeholder for retrieving a single book; not implemented yet.

## Tests and configuration

- `tests/test_api.py`: tests the status endpoint, saving single and multiple books, and rejecting invalid requests with HTTP 422 without storing data. Each test uses a fresh dictionary and FastAPI's TestClient.
- `pyproject.toml`: defines dependencies, the start command, and Ruff settings for linting and formatting.
- `uv.lock`: locks dependency versions for reproducible installations.
- `.github/workflows/ci.yml`: installs dependencies and runs Ruff lint checks, formatting checks, and pytest on every push and pull request.

## Run locally

- Requirements: Python 3.13 or later and uv.
- Install dependencies: `uv sync --locked`
- Start the API: `uv run fastapi-cicd`
- Open interactive API documentation: http://127.0.0.1:8000/docs
- Run tests: `uv run pytest -v`
- Check linting and formatting: `uv run ruff check .` and `uv run ruff format --check .`
- Fix supported lint issues and format code: `uv run ruff check --fix .` and `uv run ruff format .`


## TODo Optional

- implement a sql database instead of pythond dictionary 
- instant deployment on a raspberry pi