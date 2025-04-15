Product Catalog Filtering App
Features

- Filter products by category and tags
- Search by keywords in the product description
- Django REST Framework-powered API

Tech Stack

- Django & Django REST Framework
- HTML, CSS (Bootstrap), and JavaScript
- SQLite

Code of the backend:
in the catalog Django app
Code of the frontend:
in the templates directory 

Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/product-catalog.git
cd product-catalog

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

6. Apply migrations
python manage.py migrate

8. Create superuser
python manage.py createsuperuser

10. Run the development server
python manage.py runserver

11. Open the website page
http://127.0.0.1:8000/catalog/products-page/
