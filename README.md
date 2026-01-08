# FastAPI Async Template

A minimal async-ready FastAPI template with Docker support.

## Prerequisites

- Git
- Docker + Docker Compose (recommended)

## Clone the repository

```bash
git clone https://github.com/khasanjon-dev/FastApi-Template-Async.git
cd FastApi-Template-Async
```

## Environment variables (.env)

1. Create a `.env` file.
2. Copy values from `.env.example` and adjust them for your environment.

## Run with Docker

### Build and start

```bash
docker compose up --build

```

### Run in background

```bash
docker compose up -d --build
```

## API Documentation (Swagger / OpenAPI)

When the project is running, open Swagger UI here:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json

## API Endpoints

This project exposes its endpoints via Swagger UI.

To see the full and up-to-date list of APIs:

1. Run the project (Docker or local).
2. Open: http://localhost:8000/docs

### Stop containers

```bash
docker compose down
```

### View logs

```bash
docker compose logs -f
```