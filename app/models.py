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

    class Config:
        schema_extra = {
            "example": {
                "entrypoint": "example_entrypoint",
                "depth": 3,
                "message": "Successfully processed trace request"
            }
        }
