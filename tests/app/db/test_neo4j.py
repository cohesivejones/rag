import pytest
from unittest.mock import patch, MagicMock
from app.db.neo4j import Neo4jConnection


class TestNeo4jConnection:
    """Tests for the Neo4jConnection class."""

    def test_singleton_pattern(self):
        """Test that Neo4jConnection is a singleton."""
        conn1 = Neo4jConnection()
        conn2 = Neo4jConnection()
        assert conn1 is conn2

    @patch('app.db.neo4j.GraphDatabase')
    def test_connect(self, mock_graph_db):
        """Test the connect method."""
        # Setup
        mock_driver = MagicMock()
        mock_graph_db.driver.return_value = mock_driver
        
        # Create a new instance to reset the singleton
        Neo4jConnection._instance = None
        conn = Neo4jConnection()
        
        # Test
        conn.connect()
        
        # Assert
        mock_graph_db.driver.assert_called_once()
        assert conn.driver is mock_driver

    @patch('app.db.neo4j.GraphDatabase')
    def test_close(self, mock_graph_db):
        """Test the close method."""
        # Setup
        mock_driver = MagicMock()
        mock_graph_db.driver.return_value = mock_driver
        
        # Create a new instance to reset the singleton
        Neo4jConnection._instance = None
        conn = Neo4jConnection()
        conn.connect()
        
        # Test
        conn.close()
        
        # Assert
        mock_driver.close.assert_called_once()
        assert conn.driver is None

    @patch('app.db.neo4j.GraphDatabase')
    def test_execute_query(self, mock_graph_db):
        """Test the execute_query method."""
        # Setup
        mock_session = MagicMock()
        mock_result = MagicMock()
        mock_record1 = {"key1": "value1"}
        mock_record2 = {"key2": "value2"}
        mock_result.__iter__.return_value = [mock_record1, mock_record2]
        
        mock_session.run.return_value = mock_result
        mock_driver = MagicMock()
        mock_driver.__enter__ = MagicMock(return_value=mock_session)
        mock_driver.__exit__ = MagicMock(return_value=None)
        
        mock_graph_db.driver.return_value = MagicMock()
        mock_graph_db.driver.return_value.session.return_value = mock_driver
        
        # Create a new instance to reset the singleton
        Neo4jConnection._instance = None
        conn = Neo4jConnection()
        
        # Test
        query = "MATCH (n) RETURN n"
        params = {"param1": "value1"}
        result = conn.execute_query(query, params)
        
        # Assert
        mock_graph_db.driver.return_value.session.assert_called_once()
        mock_session.run.assert_called_once_with(query, params)
        assert result == [mock_record1, mock_record2]

    @patch('app.db.neo4j.GraphDatabase')
    def test_execute_query_error(self, mock_graph_db):
        """Test the execute_query method when an error occurs."""
        # Setup
        mock_session = MagicMock()
        mock_session.run.side_effect = Exception("Test error")
        
        mock_driver = MagicMock()
        mock_driver.__enter__ = MagicMock(return_value=mock_session)
        mock_driver.__exit__ = MagicMock(return_value=None)
        
        mock_graph_db.driver.return_value = MagicMock()
        mock_graph_db.driver.return_value.session.return_value = mock_driver
        
        # Create a new instance to reset the singleton
        Neo4jConnection._instance = None
        conn = Neo4jConnection()
        
        # Test
        query = "MATCH (n) RETURN n"
        params = {"param1": "value1"}
        
        # Assert
        with pytest.raises(Exception, match="Test error"):
            conn.execute_query(query, params)
