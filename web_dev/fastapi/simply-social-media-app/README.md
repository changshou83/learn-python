# FastAPI Course Modern

[Python API Development - Comprehensive Course for Beginners - FreeCodeCamp.org](https://www.youtube.com/watch?v=0sOvCWFmrtA) 的 2026版本（由 Codex 重写）

## Stack

- FastAPI 0.135.3
- Pydantic 2.13.2
- pydantic-settings 2.13.1
- SQLAlchemy 2.0.49
- Alembic 1.18.4
- Psycopg 3.3.3

## Features

- User registration
- JWT login
- CRUD for posts
- Vote / unvote endpoints
- Alembic migrations
- Pytest API tests

## Quick Start

1. Sync dependencies with `uv`:

```bash
uv sync --group dev
```

2. Copy the env file and adjust values:

```bash
copy .env.example .env
```

3. Run migrations:

```bash
uv run alembic upgrade head
```

4. Start the API:

```bash
uv run uvicorn app.main:app --reload
```

5. Open:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Test

```bash
uv run pytest
```

## Docker

Build and start the full stack:

```bash
docker compose up --build
```

Services:

- API behind nginx: `http://127.0.0.1:8080`
- Swagger UI: `http://127.0.0.1:8080/docs`
- Direct API container port is kept internal to compose

The compose file injects a container-safe `DATABASE_URL` that points to the `db` service, so your local `.env` can still keep `localhost` for non-Docker development.

## Gunicorn

`gunicorn` is not required for this project.

For FastAPI on Linux containers today, `uvicorn` is enough in most cases:

- single container / single process: `uvicorn`
- one container with multiple workers: `uvicorn --workers N`
- behind reverse proxy: `nginx` + `uvicorn`

`gunicorn` only becomes useful if you specifically want its process manager behavior. For this rewrite I did not add it, because it adds complexity without solving a problem that `uvicorn` and container orchestration do not already handle here.
