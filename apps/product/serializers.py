from rest_framework import serializers
from .models import Product, Gallery, Color, Order
from rest_framework import permissions

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('title','description', 'price','image','product_images','color', 'size', 'weight')

    def create(self, validated_data):
        return super().create(validated_data)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        if self.action in ['create', 'like']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['carousel'] = ProductImageSerializer(
            instance.product_images.all(), many=True
        ).data
        representation['color'] = ColorSerializer(
            instance.color.all(), many=True
        ).data
        return representation


class ProductListSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('slug','title','image')

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = 'images',
    

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

    def validate(self, attrs:dict):
        tag = attrs.get('color')
        if Color.objects.filter(title=tag).exists():
            raise serializers.ValidationError('This color already exists')
        return attrs


class OrderSerializer(serializers.ModelSerializer):


    class Meta:
        model = Order
        fields = '__all__'