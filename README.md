# Trace API

A FastAPI application that provides a `/trace` endpoint for processing trace requests.

## Project Structure

```
rag/
├── app/
│   ├── __init__.py
│   ├── main.py         # Main FastAPI application
│   ├── models.py       # Pydantic models for request/response
│   └── routers/
│       ├── __init__.py
│       └── trace.py    # Trace endpoint implementation
├── pyproject.toml      # Project configuration and dependencies
└── README.md          # Project documentation
```

## Installation

This project uses [UV](https://github.com/astral-sh/uv) for dependency management, which is a faster alternative to pip.

### Requirements

- Python 3.8.1 or higher

### Install UV

If you don't have UV installed, you can install it with:

```bash
pip install uv
```

### Set Up the Project

1. Clone the repository
2. Create a virtual environment and install dependencies:

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
uv pip install -e .

# For development, install development dependencies
uv pip install -e ".[dev]"
```

## Running the Application

To run the application locally:

```bash
# Make sure your virtual environment is activated
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Once the application is running, you can access the auto-generated API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

### POST /trace

Process a trace request with the given entrypoint and depth.

**Request Body:**

```json
{
  "entrypoint": "example_entrypoint",
  "depth": 3
}
```

**Response:**

```json
{
  "entrypoint": "example_entrypoint",
  "depth": 3,
  "message": "Successfully processed trace request for entrypoint 'example_entrypoint' with depth 3"
}
```

## Testing the API

You can test the API using curl:

```bash
curl -X 'POST' \
  'http://localhost:8000/trace' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "entrypoint": "example_entrypoint",
  "depth": 3
}'
```

Or using the Swagger UI at http://localhost:8000/docs

## Development

### Running Tests

To run tests:

```bash
# Make sure you've installed development dependencies
uv run pytest
```

To run tests with coverage:

```bash
uv run pytest --cov=app
```

### Code Formatting and Linting

This project uses:

- **Ruff** for code formatting and linting:
  ```bash
  # Format code
  uv run ruff format .
  
  # Check and auto-fix linting issues
  uv run ruff check --fix .
  ```

- **mypy** for type checking:
  ```bash
  uv run mypy app
  ```

You can run all of these checks with:

```bash
# Format and lint code
uv run ruff format .
uv run ruff check --fix .

# Type check code
uv run mypy app
```
