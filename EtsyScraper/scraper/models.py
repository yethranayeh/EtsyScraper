from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Product name"
        )
    image = models.CharField(
        max_length=250, 
        verbose_name="Product Image"
        )
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        verbose_name="Product price"
        )
    sold_out = models.BooleanField(
        default=False, 
        verbose_name="Product is sold out"
        )

    def __str__(self):
        return self.name

