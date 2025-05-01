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
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application locally:

```bash
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
