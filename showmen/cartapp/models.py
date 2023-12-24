from django.db import models
from mainapp.models import Product
# Create your models here.


class CartList(models.Model):
    cart_id = models.CharField(max_length=250, unique=True)
    date_added = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.cart_id
    
    
    
class Items(models.Model):
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.cart_product
    