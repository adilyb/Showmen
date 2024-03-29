from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse, NoReverseMatch
# Create your models here.


class ProductCategory(models.Model):
    category_name = models.CharField(max_length = 250, unique=True)
    slug = models.SlugField(max_length = 250, unique=True)
    
    class Meta:
        ordering = ["category_name"]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return '{}'.format(self.category_name)
    
    def get_url(self):
        return reverse('category_list', args=[self.slug])
    
    
class Product(models.Model):
    product_name = models.CharField(max_length = 150, unique=True)
    product_desc = models.CharField(max_length = 250, unique=True) 
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length = 250, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name
    
    def get_url(self):
        return reverse('product_detail_view', args=[self.category.slug, self.slug])
    
    
    
    
   
      
    
    


  
   


    
    
    
    