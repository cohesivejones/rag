import pytest


def test_root_endpoint(client):
    """Test that the root endpoint returns a welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Welcome to the Trace API" in data["message"]
