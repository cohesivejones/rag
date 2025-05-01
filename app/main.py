from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import trace

# Create FastAPI app
app = FastAPI(
    title="Trace API",
    description="A FastAPI application with a trace endpoint",
    version="0.1.0",
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
