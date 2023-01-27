from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, 'products')
router.register('order', OrderViewSet, 'orders')


urlpatterns = [

] + router.urls
