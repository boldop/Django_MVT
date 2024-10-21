from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    img = models.TextField()
    description = models.TextField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Product_name




