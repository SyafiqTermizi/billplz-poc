from django.db import models

from billplzshop.billplz.models import Billplzbill as Bill


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.name


class ProductBill(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='bills'
    )
    bill = models.ForeignKey(
        Bill,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
