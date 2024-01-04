from django.contrib import admin
from . models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ['category_name', 'slug', ]

admin.site.register(ProductCategory, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ['product_desc', 'image', 'price', 'stock', 'available']
    list_editable = ['image', 'price', 'stock', 'available']
    

admin.site.register(Product, ProductAdmin)
