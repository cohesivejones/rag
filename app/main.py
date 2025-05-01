from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import trace
from app.db.neo4j import neo4j_connection
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager

# Load environment variables from .env file
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: connect to Neo4j
    neo4j_connection.connect()
    yield
    # Shutdown: close Neo4j connection
    neo4j_connection.close()

# Create FastAPI app
app = FastAPI(
    title="Trace API",
    description="A FastAPI application with a trace endpoint",
    version="0.1.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(trace.router)


@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Trace API. Use /docs to see the API documentation."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
