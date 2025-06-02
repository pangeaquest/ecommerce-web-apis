"""
Product Controller - Handles business logic for product operations
Step 8: Implement business logic in Product controller
"""
from flask import request
from typing import Dict, List, Tuple
import logging

from models.product_model import ProductModel
from views.product_views import ProductViews

logger = logging.getLogger(__name__)

class ProductController:
    def __init__(self):
        """
        TODO: Initialize ProductController
        - Create ProductModel instance
        - Create ProductViews instance
        """
        # TODO: Implement initialization
        pass

    def add_product(self) -> Tuple:
        """
        TODO: Handle product creation request
        - Check if request is JSON
        - Get JSON data from request
        - Validate data is provided
        - Call product_model.create_product()
        - Return formatted response using product_views
        - Handle ValueError and general exceptions
        """
        # TODO: Implement add_product method
        pass

    def update_product(self, product_id: str) -> Tuple:
        """
        TODO: Handle product update request
        - Validate product_id is provided
        - Check if request is JSON
        - Get JSON data from request
        - Call product_model.update_product()
        - Handle product not found case
        - Return formatted response using product_views
        - Handle ValueError and general exceptions
        """
        # TODO: Implement update_product method
        pass

    def delete_product(self, product_id: str) -> Tuple:
        """
        TODO: Handle product deletion request
        - Validate product_id is provided
        - Call product_model.delete_product()
        - Handle product not found case
        - Return formatted response using product_views
        - Handle general exceptions
        """
        # TODO: Implement delete_product method
        pass

    def get_product(self, product_id: str) -> Tuple:
        """
        TODO: Handle get single product request
        - Validate product_id is provided
        - Call product_model.get_product()
        - Handle product not found case
        - Return formatted response using product_views
        - Handle general exceptions
        """
        # TODO: Implement get_product method
        pass

    def get_all_products(self) -> Tuple:
        """
        TODO: Handle get all products request
        - Get pagination parameters (limit, skip) from request.args
        - Validate pagination parameters (limit 1-1000, skip >= 0)
        - Call product_model.get_all_products()
        - Return formatted response using product_views
        - Handle general exceptions
        """
        # TODO: Implement get_all_products method
        pass
