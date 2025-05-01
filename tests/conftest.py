import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.neo4j import neo4j_connection


@pytest.fixture
def client():
    """
    Create a test client for the FastAPI application.
    """
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def mock_neo4j_connection(monkeypatch):
    """
    Mock the Neo4j connection to avoid actual database calls during tests.
    This fixture is automatically used in all tests.
    """
    def mock_execute_query(query, params=None):
        """Mock implementation of execute_query that returns test data."""
        # Return mock data based on the query parameters
        entrypoint = params.get("entrypoint", "default_entrypoint")
        depth = params.get("depth", 1)
        
        # Generate mock results
        return [
            {"source": entrypoint, "target": f"mock_node_{i}", "distance": min(i, depth)} 
            for i in range(1, min(5, depth + 1))
        ]
    
    # Replace the execute_query method with our mock implementation
    monkeypatch.setattr(neo4j_connection, "execute_query", mock_execute_query)
    
    # Mock the connect and close methods to do nothing
    monkeypatch.setattr(neo4j_connection, "connect", lambda: None)
    monkeypatch.setattr(neo4j_connection, "close", lambda: None)
