"""
Product Model - Handles all database operations for products
Step 5 & 6: Create Product data model with validation and CRUD operations
"""
import uuid
from datetime import datetime
from typing import Dict, List, Optional
from bson import ObjectId
from pymongo.errors import DuplicateKeyError, PyMongoError
import logging

from .database import get_collection

logger = logging.getLogger(__name__)

class ProductModel:
    def __init__(self):
        """
        TODO: Initialize ProductModel
        - Get 'productDetails' collection using get_collection()
        - Create unique index on 'productId' field for faster queries
        """
        # TODO: Implement initialization
        pass

    def _generate_product_id(self) -> str:
        """
        TODO: Generate a unique product ID
        - Use uuid.uuid4() to generate unique ID
        - Convert to string and return
        """
        # TODO: Implement product ID generation
        pass

    def _validate_product_data(self, product_data: Dict) -> Dict:
        """
        TODO: Validate and sanitize product data
        - Check required fields: manufacturer, productDescription, price
        - Validate price is non-negative number
        - Validate avgStarRating is between 1-5 if provided
        - Raise ValueError for invalid data
        - Return validated data
        """
        # TODO: Implement data validation logic
        pass

    def create_product(self, product_data: Dict) -> Dict:
        """
        TODO: Create a new product
        - Validate product data using _validate_product_data()
        - Generate unique product ID
        - Add createdAt and updatedAt timestamps
        - Insert into MongoDB collection
        - Handle DuplicateKeyError and PyMongoError exceptions
        - Return created product without MongoDB _id field
        """
        # TODO: Implement create_product method
        pass

    def get_product(self, product_id: str) -> Optional[Dict]:
        """
        TODO: Get a product by ID
        - Query collection by productId
        - Exclude MongoDB _id field from result
        - Handle PyMongoError exceptions
        - Return product or None if not found
        """
        # TODO: Implement get_product method
        pass

    def update_product(self, product_id: str, update_data: Dict) -> Optional[Dict]:
        """
        TODO: Update a product by ID
        - Remove productId from update_data if present
        - Validate update data
        - Add updatedAt timestamp
        - Use $set operator to update document
        - Return updated product or None if not found
        - Handle PyMongoError exceptions
        """
        # TODO: Implement update_product method
        pass

    def delete_product(self, product_id: str) -> bool:
        """
        TODO: Delete a product by ID
        - Use delete_one() to remove product by productId
        - Return True if deleted, False if not found
        - Handle PyMongoError exceptions
        """
        # TODO: Implement delete_product method
        pass

    def get_all_products(self, limit: int = 100, skip: int = 0) -> List[Dict]:
        """
        TODO: Get all products with pagination
        - Query collection with skip() and limit()
        - Exclude MongoDB _id field from results
        - Return list of products
        - Handle PyMongoError exceptions
        """
        # TODO: Implement get_all_products method
        pass
