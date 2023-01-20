from django.db import models
from ..product.models import Product

class Payment(models.Model):
    card_number = models.IntegerField()
    card_data = models.DateField()
    username = models.CharField(max_length=50)
    security_code = models.IntegerField()

    def __str__(self) -> str:
        return self.id


class Order(models.Model):
    address = models.CharField(max_length=200)
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='order'
    )
    quantity = models.IntegerField()
    is_payed = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.product