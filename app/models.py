from django.db import models

class Product(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    quantity = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)