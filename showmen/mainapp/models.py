from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class ProductCategory(models.Model):
    category_name = models.CharField(max_length = 250, unique=True)
    slug = models.SlugField(max_length = 250, unique=True)
    
    
class Product(models.Model):
    product_name = models.CharField(max_length = 150, unique=True)
    product_desc = models.CharField(max_length = 250, unique=True) 
    # image = models.ImageField(upload_to='product_image')
    price = models.IntegerField()
    stock = models.IntegerField()
    slug = models.SlugField(max_length = 250, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    
   


    
    
    
    