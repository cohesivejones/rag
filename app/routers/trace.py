from fastapi import APIRouter, Body
from app.models import TraceRequest, TraceResponse

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
    # Process the request (in a real application, this would contain actual logic)
    # For now, we'll just echo back the parameters
    
    return TraceResponse(
        entrypoint=request.entrypoint,
        depth=request.depth,
        message=f"Successfully processed trace request for entrypoint '{request.entrypoint}' with depth {request.depth}"
    )
