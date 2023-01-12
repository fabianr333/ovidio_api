from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(max_length=8)
    name = models.CharField(max_length=40)
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


