from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)