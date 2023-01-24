from django.contrib import admin
from .models import Product, Gallery, Color

admin.site.register(Color)

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]