from django.shortcuts import render, get_object_or_404
from . models import *
from django.db.models import Q
    
def store(request, slug_url=None):
        
    categ_slug_var = None
    prod_filter_var = None
    
    if slug_url != None:
        categ_slug_var = get_object_or_404(ProductCategory, slug=slug_url)
        prod_filter_var = Product.objects.filter(category=categ_slug_var, available=True)
        
    else:
        prod_filter_var = Product.objects.all().filter(available=True)
    
    context = {'prod':prod_filter_var}
    return render(request, 'mainapp/store.html', context)


def category_list(request): 
    queryset = ProductCategory.objects.all()
    
    context = {'categorylist':queryset}
    return render(request, 'mainapp/main.html', context)

def product_view(request, slug_url, product_slug):
    try:
        prod = Product.objects.get(category__slug=slug_url, slug=product_slug)
        
    except Exception as e:
        raise e
    
    return render(request, "mainapp/product_view.html", {'prod': prod})


def search(request):
    
    query = None
    result = None
    if "q" in request.GET:
        query = request.GET['q']
        result = Product.objects.all().filter(Q(product_name__icontains=query) | Q(product_desc__icontains=query))
    else:
        result = Product.objects.all()
        
    context = {'result': result}
    return render(request, "mainapp/search.html", context)