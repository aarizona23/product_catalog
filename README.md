Product Catalog Filtering App

## Features

- Filter products by category and tags  
- Search by keywords in the product description  
- Django REST Framework-powered API  

## Tech Stack

- Django & Django REST Framework  
- HTML, CSS (Bootstrap), and JavaScript  
- SQLite  

## 📂 Code Structure

**Backend:** in the `catalog` Django app  
**Frontend:** in the `templates` directory  

## ⚙️ Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/product-catalog.git  
cd product-catalog
```

2. Create and activate a virtual environment

```bash
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Apply migrations

```bash
python manage.py migrate
```

5. Create superuser

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

7. Open the website page
http://127.0.0.1:8000/catalog/products-page/
