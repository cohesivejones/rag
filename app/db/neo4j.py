from neo4j import GraphDatabase
from typing import Dict, Any, List
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

class Neo4jConnection:
    """
    Neo4j database connection handler.
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Neo4jConnection, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance
    
    def __init__(self):
        if self.initialized:
            return
            
        self.uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.user = os.getenv("NEO4J_USER", "neo4j")
        self.password = os.getenv("NEO4J_PASSWORD", "password")
        self.driver = None
        self.initialized = True
        
    def connect(self):
        """Connect to Neo4j database."""
        if not self.driver:
            try:
                self.driver = GraphDatabase.driver(
                    self.uri, 
                    auth=(self.user, self.password)
                )
                logger.info(f"Connected to Neo4j database at {self.uri}")
            except Exception as e:
                logger.error(f"Failed to connect to Neo4j database: {str(e)}")
                raise
        
    def close(self):
        """Close the Neo4j driver connection."""
        if self.driver:
            self.driver.close()
            self.driver = None
            logger.info("Disconnected from Neo4j database")
        
    def execute_query(self, query: str, params: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Execute a Cypher query and return the results.
        
        Args:
            query: The Cypher query to execute
            params: Parameters for the query
            
        Returns:
            List of records as dictionaries
        """
        if not self.driver:
            self.connect()
            
        try:
            with self.driver.session() as session:
                result = session.run(query, params)
                return [dict(record) for record in result]
        except Exception as e:
            logger.error(f"Neo4j query error: {str(e)}")
            raise

# Create a singleton instance
neo4j_connection = Neo4jConnection()
