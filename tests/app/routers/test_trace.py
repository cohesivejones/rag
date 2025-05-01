import pytest


def test_trace_endpoint(client):
    """Test that the trace endpoint returns the expected response."""
    response = client.post(
        "/trace",
        json={"entrypoint": "test_entrypoint", "depth": 2},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["entrypoint"] == "test_entrypoint"
    assert data["depth"] == 2
    assert "message" in data
    assert "results" in data


def test_trace_endpoint_validation(client):
    """Test that the trace endpoint validates input correctly."""
    # Test with missing entrypoint
    response = client.post(
        "/trace",
        json={"depth": 2},
    )
    assert response.status_code == 422

    # Test with missing depth
    response = client.post(
        "/trace",
        json={"entrypoint": "test_entrypoint"},
    )
    assert response.status_code == 422

    # Test with negative depth
    response = client.post(
        "/trace",
        json={"entrypoint": "test_entrypoint", "depth": -1},
    )
    assert response.status_code == 422
