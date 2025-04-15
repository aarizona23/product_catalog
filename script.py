import os
import sys
import django

# Get the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project directory to the Python path
sys.path.append(BASE_DIR)

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "product_catalog.settings")  # Update this with your actual settings module
django.setup()

from catalog.models import ProductModel, CategoryModel, TagModel
import random

if __name__ == "__main__":
    # Create Categories
    categories_data = [
        "Electronics",
        "Books",
        "Clothing",
        "Home & Kitchen",
        "Sports & Outdoors"
    ]
    categories = [CategoryModel.objects.create(name=cat) for cat in categories_data]

    # Create Tags
    tags_data = [
        "New",
        "Sale",
        "Popular",
        "Limited Edition",
        "Best Seller"
    ]
    tags = [TagModel.objects.create(name=tag) for tag in tags_data]

    # Product Data (20 Products)
    products_data = [
        ("Wireless Headphones", "High-quality sound with noise cancellation.", "Electronics"),
        ("Smartphone", "Latest model with powerful features.", "Electronics"),
        ("Cookbook", "Healthy and delicious recipes.", "Books"),
        ("Running Shoes", "Comfortable and durable for long runs.", "Clothing"),
        ("LED Desk Lamp", "Adjustable brightness for optimal lighting.", "Home & Kitchen"),
        ("Stainless Steel Water Bottle", "Keeps drinks cold for 24 hours.", "Sports & Outdoors"),
        ("Yoga Mat", "Non-slip surface with extra padding.", "Sports & Outdoors"),
        ("Bluetooth Speaker", "Portable with great bass.", "Electronics"),
        ("Fiction Novel", "A thrilling story that keeps you hooked.", "Books"),
        ("Men's Jacket", "Warm and stylish for winter.", "Clothing"),
        ("Women's T-Shirt", "Soft cotton with printed design.", "Clothing"),
        ("Blender", "Perfect for smoothies and shakes.", "Home & Kitchen"),
        ("Camping Tent", "Spacious and easy to set up.", "Sports & Outdoors"),
        ("Wireless Mouse", "Ergonomic and responsive.", "Electronics"),
        ("Notebook", "Lined pages with hardcover.", "Books"),
        ("Coffee Maker", "Brews the perfect cup every time.", "Home & Kitchen"),
        ("Action Camera", "Capture your adventures in HD.", "Electronics"),
        ("Backpack", "Ideal for travel and daily use.", "Clothing"),
        ("Cookware Set", "Non-stick and dishwasher-safe.", "Home & Kitchen"),
        ("Basketball", "Official size and weight.", "Sports & Outdoors")
    ]

    # Create Products
    for name, description, category_name in products_data:
        category = CategoryModel.objects.get(name=category_name)
        product = ProductModel.objects.create(name=name, description=description, category=category)
        # Assign random tags to products
        product.tags.set(random.sample(tags, random.randint(2, 4)))
        product.save()

    print("Sample data created successfully.")

