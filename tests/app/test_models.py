import pytest
from pydantic import ValidationError
from app.models import TraceRequest, TraceResponse


def test_trace_request_model():
    """Test that the TraceRequest model validates input correctly."""
    # Valid input
    request = TraceRequest(entrypoint="test_entrypoint", depth=2)
    assert request.entrypoint == "test_entrypoint"
    assert request.depth == 2

    # Invalid depth (negative)
    with pytest.raises(ValidationError):
        TraceRequest(entrypoint="test_entrypoint", depth=-1)

    # Missing entrypoint
    with pytest.raises(ValidationError):
        TraceRequest(depth=2)

    # Missing depth
    with pytest.raises(ValidationError):
        TraceRequest(entrypoint="test_entrypoint")


def test_trace_response_model():
    """Test that the TraceResponse model works correctly."""
    # Basic response
    response = TraceResponse(
        entrypoint="test_entrypoint",
        depth=2,
        message="Test message",
    )
    assert response.entrypoint == "test_entrypoint"
    assert response.depth == 2
    assert response.message == "Test message"
    assert response.results == []

    # Response with results
    results = [
        {"source": "test_entrypoint", "target": "node1", "distance": 1},
        {"source": "test_entrypoint", "target": "node2", "distance": 2},
    ]
    response = TraceResponse(
        entrypoint="test_entrypoint",
        depth=2,
        message="Test message",
        results=results,
    )
    assert response.results == results
