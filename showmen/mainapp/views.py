from django.shortcuts import render, get_object_or_404
from . models import *
# Create your views here.



    
def store(request, slug_url=None):
    categ_slug_var = None
    prod_filter_var = None
    
    if slug_url != None:
        categ_slug_var = get_object_or_404(ProductCategory, slug=slug_url)
        prod_filter_var = Product.objects.filter(category=categ_slug_var, available=True)
        
    else:
        prod_filter_var = Product.objects.all().filter(available=True)
        
    categ_breadcomb = ProductCategory.objects.all()
    return render(request, 'mainapp/store.html',{'prod':prod_filter_var, 'cat':categ_breadcomb})

def cat(request): 
    categ_breadcomb = ProductCategory.objects.all()
    return render(request, 'mainapp/main.html',{'cat':categ_breadcomb})

def product_view(request, slug_url, product_slug):
    try:
        prod_filter_var = Product.objects.get(category_slug = slug_url )
    except Exception as e:
        raise e
        
    
    return render(request, "mainapp/product_view.html", {'product': prod_filter_var})


