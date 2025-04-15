from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('products-page/', product_list_view, name='product-list'),
    path('api/products/', GetProductsView.as_view(), name='get_products'),
    path('api/categories/', GetCategoriesView.as_view(), name='get_categories'),
    path('api/tags/', GetTagsView.as_view(), name='get_tags')
    ]