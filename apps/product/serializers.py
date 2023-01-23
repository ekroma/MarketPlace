from rest_framework import serializers
from .models import Product
from rest_framework import permissions

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('image', 'title','description', 'price')

    def create(self, validated_data):
        return super().create(validated_data)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        if self.action in ['create', 'like']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

class ProductListSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('slug','image', 'title',)
