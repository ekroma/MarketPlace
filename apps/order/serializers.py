from rest_framework import serializers
from .models import Order, Payment


class OrderSerializer(serializers.ModelSerializer):


    class Meta:
        model = Order
        fields = '__all__'

    