from django.db import models

class TagModel(models.Model):
    """
    Represents a tag for a product.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CategoryModel(models.Model):
    """
    Represents a category for a product.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    """
    Represents a product.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(TagModel, related_name='products')
    category = models.ForeignKey(CategoryModel, related_name='products', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name