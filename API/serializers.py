from rest_framework import serializers
from Product_app.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'warranty', 'product_type', 'brand', 'product_name', 'product_title',
                  'price', 'stock', 'is_available', 'image']