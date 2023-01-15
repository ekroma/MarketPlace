from email.mime import image
from django.db import models
from slugify import slugify
from .utils import get_time

class Product(models.Model):
    title = models.CharField('Title', max_length=200)
    slug = models.SlugField('Slug', max_length=220, primary_key=True, blank=True)
    image = models.ImageField(
        upload_to='product/image',
    )
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + get_time())
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title