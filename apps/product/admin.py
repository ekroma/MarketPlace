from django.contrib import admin
from .models import Product, Gallery, Color, Order

admin.site.register([Color, Order])

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]