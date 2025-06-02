"""
Database configuration and connection setup for MongoDB
Step 4: Implement MongoDB database connection and configuration
"""
import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database:
    """
    TODO: Implement Database class with singleton pattern
    - Create class variables: _instance, _client, _db
    - Implement __new__ method for singleton pattern
    - Implement __init__ method to initialize connection
    """
    # TODO: Add singleton pattern implementation here
    pass

    def connect(self):
        """
        TODO: Establish connection to MongoDB
        - Get MongoDB URI from environment variables (default: mongodb://localhost:27017/)
        - Get database name from environment variables (default: ecommerce_db)
        - Create MongoClient instance
        - Test connection with ping command
        - Handle ConnectionFailure and other exceptions
        """
        # TODO: Implement MongoDB connection logic here
        pass

    def get_database(self):
        """
        TODO: Get the database instance
        - Check if database is None, if so call connect()
        - Return database instance
        """
        # TODO: Implement get_database method
        pass

    def get_collection(self, collection_name):
        """
        TODO: Get a specific collection
        - Get database instance
        - Return collection by name
        """
        # TODO: Implement get_collection method
        pass

    def close_connection(self):
        """
        TODO: Close the database connection
        - Check if client exists
        - Close client connection
        - Log connection closure
        """
        # TODO: Implement connection closure
        pass

# TODO: Create global database instance
# db_instance = Database()

def get_db():
    """
    TODO: Get database instance
    - Return database from global instance
    """
    # TODO: Implement get_db function
    pass

def get_collection(collection_name):
    """
    TODO: Get a specific collection
    - Return collection from global instance
    """
    # TODO: Implement get_collection function
    pass
