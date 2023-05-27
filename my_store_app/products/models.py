from math import prod
from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=255)
    productPrice = models.DecimalField(decimal_places=1, max_digits=5)
    productCount = models.IntegerField()