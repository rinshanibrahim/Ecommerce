from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    selling_price = models.FloatField(max_length=200, null=True)
    discount_price = models.FloatField(max_length=200,null=True)
    description = models.TextField(max_length=200, null=True)
    apppro = models.TextField(max_length=200, null=True)
    category = models.CharField(max_length=2)
    product_image = models.ImageField(upload_to='product')
    
    def __str__(self):
        return self.title
    
