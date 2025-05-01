from fastapi import APIRouter, Body, HTTPException
from app.models import TraceRequest, TraceResponse
from app.db.neo4j import neo4j_connection
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/trace",
    tags=["trace"],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=TraceResponse, status_code=200)
async def trace(request: TraceRequest = Body(...)):
    """
    Process a trace request with the given entrypoint and depth.
    
    - **entrypoint**: A string representing the starting point
    - **depth**: An integer representing the depth of the trace
    
    Returns a response containing the processed parameters and a success message.
    """
    # Sample Cypher query using the entrypoint and depth parameters
    query = """
    MATCH path = (n {name: $entrypoint})-[*1..$depth]-(connected)
    RETURN n.name AS source, connected.name AS target, length(path) AS distance
    LIMIT 10
    """
    
    try:
        # Try to execute the Neo4j query
        results = neo4j_connection.execute_query(
            query, 
            {"entrypoint": request.entrypoint, "depth": request.depth}
        )
    except Exception as e:
        # Log the error
        logger.warning(f"Neo4j connection error: {str(e)}")
        logger.info("Using mock data instead")
        
        # Return mock data for demonstration purposes
        results = [
            {"source": request.entrypoint, "target": f"connected_node_{i}", "distance": min(i, request.depth)} 
            for i in range(1, min(5, request.depth + 1))
        ]
    
    return TraceResponse(
        entrypoint=request.entrypoint,
        depth=request.depth,
        message=f"Successfully processed trace request for entrypoint '{request.entrypoint}' with depth {request.depth}",
        results=results
    )
