from typing import Any, Dict, List

from pydantic import BaseModel, Field


class TraceRequest(BaseModel):
    """
    Request model for the trace endpoint.
    """
    entrypoint: str = Field(..., description="The entrypoint string")
    depth: int = Field(..., description="The depth integer", ge=0)

    class Config:
        schema_extra = {
            "example": {
                "entrypoint": "example_entrypoint",
                "depth": 3
            }
        }


class TraceResponse(BaseModel):
    """
    Response model for the trace endpoint.
    """
    entrypoint: str
    depth: int
    message: str
    results: List[Dict[str, Any]] = Field(
        default_factory=list, 
        description="Neo4j query results"
    )

    class Config:
        schema_extra = {
            "example": {
                "entrypoint": "example_entrypoint",
                "depth": 3,
                "message": "Successfully processed trace request",
                "results": [
                    {
                        "source": "example_entrypoint", 
                        "target": "connected_node", 
                        "distance": 1
                    }
                ]
            }
        }
