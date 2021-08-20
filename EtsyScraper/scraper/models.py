from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
