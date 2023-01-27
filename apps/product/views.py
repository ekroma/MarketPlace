from .models import Order
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters import rest_framework as rest_filter
from .models import Product
from .serializers import ProductListSerialiers, ProductSerializer, OrderSerializer
from rest_framework import permissions


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter, rest_filter.DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title']
    # filterset_fields = ['category']
    # ordering_fields = ['category']
    permission_classes = [permissions.AllowAny]


    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerialiers
        return ProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
