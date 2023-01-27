from django.db import models
from slugify import slugify
from .utils import get_time
from django.contrib.auth import get_user_model

User = get_user_model()


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
    size = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + get_time())
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
class Gallery(models.Model):
    images = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')


class Order(models.Model):
    """ Заказ """
    adress = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    card = models.CharField(max_length=16)
    quantity = models.PositiveIntegerField(default=1, blank=True)
    final_price = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.final_price = self.quantity * self.product.price
        if not self.adress and not self.user.adress:
            raise ValueError('write adress')
        if not self.adress:
            self.adress = self.user.adress
        super().save(*args, **kwargs)

    def __str__(self):
        return "Объект: {} (заказ)".format(self.product.title)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

