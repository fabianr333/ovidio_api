from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=40)

class Product(models.Model):
    sku = models.CharField(max_length=8)
    name = models.CharField(max_length=40)
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


