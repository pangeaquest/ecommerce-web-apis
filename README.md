# Ecommerce Web APIs - Project Template

A guided template for building a complete ecommerce product management system with Python Flask backend and HTML/CSS/JavaScript frontend, following MVC (Model-View-Controller) architecture.

## 🚧 This is a Template Project

This repository contains a structured template with TODO comments and guidance for implementing a full-stack ecommerce API system. Follow the step-by-step instructions in each file to build the complete application.

## 📋 How to Use This Template

1. **Follow the Step-by-Step Guide**: Each file contains detailed TODO comments that correspond to the 12 implementation steps
2. **Start with Step 1**: Set up MongoDB and your development environment
3. **Implement Each Component**: Work through models, views, controllers, and frontend in order
4. **Test Your Progress**: Use the test scripts to verify each component works correctly
5. **Complete the Project**: Follow all steps to build a fully functional ecommerce API system

## 🎯 Learning Objectives

By completing this template, you will learn:
- **MVC Architecture**: Proper separation of concerns in web applications
- **RESTful API Design**: Creating clean, consistent API endpoints
- **MongoDB Integration**: Database operations and data modeling
- **Flask Development**: Building robust web applications with Python
- **Frontend Integration**: Creating interactive web interfaces
- **Testing Strategies**: Implementing comprehensive testing for APIs

## Features to Implement

- **RESTful APIs** for product management (CRUD operations)
- **MVC Architecture** with clear separation of concerns
- **MongoDB** integration for data persistence
- **Simple Web UI** for testing all API endpoints
- **Comprehensive error handling** and validation
- **CORS enabled** for cross-origin requests

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/products` | Add a new product |
| GET | `/api/products` | Get all products |
| GET | `/api/products/<productId>` | Get a specific product |
| PUT | `/api/products/<productId>` | Update a product |
| DELETE | `/api/products/<productId>` | Delete a product |
| GET | `/health` | Health check endpoint |

## Project Structure

```
ecommerce-web-apis/
├── models/
│   ├── database.py          # MongoDB connection setup
│   └── product_model.py     # Product data model and operations
├── views/
│   └── product_views.py     # Response formatting (JSON views)
├── controllers/
│   └── product_controller.py # Business logic and request handling
├── frontend/
│   ├── index.html           # Main UI page
│   ├── style.css           # Styling
│   └── script.js           # Frontend JavaScript
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## Prerequisites

1. **Python 3.7+** installed on your system
2. **MongoDB** installed and running locally
   - Download from: https://www.mongodb.com/try/download/community
   - Default connection: `mongodb://localhost:27017/`

## Setup Instructions

### 1. Clone and Navigate to Project
```bash
cd ecommerce-web-apis
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment (Optional)
```bash
cp .env.example .env
# Edit .env file if you need to change default settings
```

### 5. Start MongoDB
Make sure MongoDB is running on your system:
```bash
# On macOS with Homebrew
brew services start mongodb-community

# On Windows (if installed as service)
net start MongoDB

# Or run manually
mongod
```

## Running the Application

### Start the Backend Server
```bash
python app.py
```

The server will start on `http://127.0.0.1:5000` by default.

You should see output like:
```
Starting Ecommerce API server on 127.0.0.1:5000
Debug mode: True
Frontend available at: http://127.0.0.1:5000
API endpoints available at: http://127.0.0.1:5000/api/products
```

### Access the Frontend UI
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

The web interface provides forms to test all API endpoints:
- ✅ Check API status
- ➕ Add new products
- 📋 View all products
- 🔍 Get single product by ID
- ✏️ Update existing products
- 🗑️ Delete products

## Product Data Schema

```json
{
  "productId": "auto-generated-uuid",
  "manufacturer": "string (required)",
  "productDescription": "string (required)",
  "price": "number (required, >= 0)",
  "avgStarRating": "number (optional, 1-5)",
  "category": "string (optional)",
  "stockQuantity": "number (optional, >= 0)",
  "createdAt": "datetime (auto-generated)",
  "updatedAt": "datetime (auto-updated)"
}
```

## API Usage Examples

### Add Product
```bash
curl -X POST http://127.0.0.1:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{
    "manufacturer": "Apple",
    "productDescription": "iPhone 15 Pro Max",
    "price": 1199.99,
    "avgStarRating": 4.8,
    "category": "Electronics"
  }'
```

### Get All Products
```bash
curl http://127.0.0.1:5000/api/products
```

### Update Product
```bash
curl -X PUT http://127.0.0.1:5000/api/products/<productId> \
  -H "Content-Type: application/json" \
  -d '{
    "price": 1099.99,
    "avgStarRating": 4.9
  }'
```

### Delete Product
```bash
curl -X DELETE http://127.0.0.1:5000/api/products/<productId>
```

## Development

### MVC Architecture

- **Models** (`models/`): Handle data operations and database interactions
- **Views** (`views/`): Format responses and handle presentation logic
- **Controllers** (`controllers/`): Process requests and coordinate between models and views

### Adding New Features

1. **Model**: Add data operations in `models/product_model.py`
2. **View**: Add response formatting in `views/product_views.py`
3. **Controller**: Add business logic in `controllers/product_controller.py`
4. **Routes**: Add new endpoints in `app.py`

## Troubleshooting

### MongoDB Connection Issues
- Ensure MongoDB is running: `mongod --version`
- Check connection string in `.env` file
- Verify MongoDB is accessible on default port 27017

### Port Already in Use
- Change the PORT in `.env` file
- Or kill the process using the port: `lsof -ti:5000 | xargs kill -9`

### CORS Issues
- CORS is enabled by default for all origins
- Modify CORS settings in `app.py` if needed

## License

This project is open source and available under the MIT License.