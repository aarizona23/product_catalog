from rest_framework import serializers
from .models import *

class TagModelSerializer(serializers.ModelSerializer):
    """
    Serializer for the TagModel.
    """
    class Meta:
        model = TagModel
        fields = ['id', 'name']
        read_only_fields = ['id']

class CategoryModelSerializer(serializers.ModelSerializer):
    """
    Serializer for the CategoryModel.
    """
    class Meta:
        model = CategoryModel
        fields = ['id', 'name']
        read_only_fields = ['id']

class ProductModelSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductModel.
    """
    tag_names = TagModelSerializer(many=True, source='tags')
    category_name = CategoryModelSerializer(source='category')

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'description', 'tag_names', 'category_name']
        read_only_fields = ['id']

class GetFilterSerializer(serializers.Serializer):
    """
    Serializer for the GET request to filter products.
    """
    category_id = serializers.IntegerField(required=False)
    tag_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    query = serializers.CharField(required=False)

    def validate(self, attrs):
        """
        Validate the input data.
        """
        attrs = super().validate(attrs)
        category_id = attrs.get('category_id', None)
        tag_ids = attrs.get('tag_ids', None)

        # Get the category from id
        if category_id:
            try:
                attrs['category'] = CategoryModel.objects.get(id=category_id)
            except CategoryModel.DoesNotExist:
                raise serializers.ValidationError('Category does not exist.')

        # Get the tags from ids
        if tag_ids:
            tags = TagModel.objects.filter(id__in=tag_ids)

            # Check if all tags exist
            if len(tags) != len(tag_ids):
                raise serializers.ValidationError('Some tags do not exist.')
            attrs['tags'] = tags
        return attrs

