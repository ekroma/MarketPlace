from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('image', 'title','description', 'price')

    def create(self, validated_data):
        return super().create(validated_data)


class ProductListSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('slug','image', 'title',)
