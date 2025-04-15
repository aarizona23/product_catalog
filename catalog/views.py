from urllib.request import Request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductModel, CategoryModel, TagModel
from .serializers import GetFilterSerializer, ProductModelSerializer, CategoryModelSerializer, TagModelSerializer

def product_list_view(request):
    return render(request, 'catalog/product_list.html')

class GetProductsView(APIView):
    def post(self, request: Request):
        """
        Get products based on filters and search query.
        """
        serializer = GetFilterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category = serializer.validated_data.get('category')
        tags = serializer.validated_data.get('tags', [])
        query = serializer.validated_data.get('query', '')

        products = ProductModel.objects.all()

        if category:
            products = products.filter(category=category)

        if tags:
            products = products.filter(tags__in=tags).distinct()

        if query:
            for word in query.split():
                products = products.filter(description__icontains=word)

        if not products.exists():
            return Response({"message": "No products found."}, status=status.HTTP_404_NOT_FOUND)

        serialized = ProductModelSerializer(products, many=True).data
        return Response(serialized, status=status.HTTP_200_OK)


class GetCategoriesView(APIView):
    def get(self, request: Request):
        """
        Get all categories.
        """
        categories = CategoryModel.objects.all()
        return Response(CategoryModelSerializer(categories, many=True).data, status=status.HTTP_200_OK)

class GetTagsView(APIView):
    def get(self, request: Request):
        """
        Get all tags.
        """
        tags = TagModel.objects.all()
        return Response(TagModelSerializer(tags, many=True).data, status=status.HTTP_200_OK)