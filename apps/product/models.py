from email.mime import image
from django.db import models
from slugify import slugify
from .utils import get_time



class Color(models.Model):
    color = models.CharField(max_length=30, unique=True)
    
    
    def __str__(self):
        return self.color


class Product(models.Model):
    title = models.CharField('Title', max_length=200)
    slug = models.SlugField('Slug', max_length=220, primary_key=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    in_stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product/image', blank=True)
    color = models.ManyToManyField(
        to=Color,
        related_name='product',
        blank=True
    )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + get_time())
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
class Gallery(models.Model):
    images = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')