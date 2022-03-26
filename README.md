# harubooru

Harubooru is a simple, API based image board server.

## Getting Started

This project uses [poetry](https://python-poetry.org) for dependency management and environment isolation.

Install dependencies including for development:

```shell
poetry install
```

For production use, add `--no-dev` to omit development dependencies.

Run local development server inside poetry virtual environment:

```shell
poetry run uvicorn main:app --app-dir src --reload
```
