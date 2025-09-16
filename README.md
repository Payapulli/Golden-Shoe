# Golden Shoe - E-commerce Platform

A modern e-commerce web application built with Flask for selling shoes and footwear. This application demonstrates core e-commerce functionality including user authentication, product catalog, shopping cart, and order management.

## Features

- User Authentication: Complete user registration, login, and account management
- Product Catalog: Browse shoes with detailed product pages and multiple images
- Shopping Cart: Add/remove items, quantity management, and cart persistence
- Search Functionality: Search products by name with real-time results
- Size Selection: Multiple size options for each product type
- Stock Management: Real-time inventory tracking and stock validation
- Responsive Design: Mobile-friendly Bootstrap UI with modern styling
- Order Processing: Complete checkout flow with stock updates

## Tech Stack

- Backend: Flask (Python)
- Database: SQLite with SQLAlchemy ORM
- Frontend: HTML5, CSS3, Bootstrap 4, JavaScript
- Authentication: Flask-Login with password hashing
- Forms: Flask-WTF with WTForms validation
- Security: Bcrypt for password hashing

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python run.py
```

Open your browser to: `http://127.0.0.1:5000`

### Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Install and run
pip install -r requirements.txt
python run.py
```

## Database Schema

- Users: User accounts with authentication and profile information
- Products: Product catalog with images, pricing, and inventory
- Cart: Shopping cart items linked to users and products
```

## Configuration

The application uses environment variables for configuration. Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///golden_shoe.db
```

## Usage

1. Browse Products: Visit the home page to see featured products
2. Search: Use the search bar to find specific products
3. Register/Login: Create an account or login to access cart functionality
4. Add to Cart: Select size and quantity, then add items to cart
5. Checkout: Review cart items and complete your order

## Security Features

- Password hashing with Bcrypt
- CSRF protection on forms
- User session management
- Input validation and sanitization

## Responsive Design

The application is fully responsive and works seamlessly across desktop computers, tablets, and mobile phones.