from django.shortcuts import render, get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator
    
    
    
def store(request, slug_url=None):
        
    categ_slug_var = None
    product_list = None
    
    if slug_url != None:
        categ_slug_var = get_object_or_404(ProductCategory, slug=slug_url)
        product_list = Product.objects.filter(category=categ_slug_var, available=True)
        
    else:
        product_list = Product.objects.all().filter(available=True)
        paginator = Paginator(product_list, 6)
        try:
            page=int(request.GET.get('page', '1'))
        except:
            page=1
        try:
            product=paginator.page(page)
        except:
            product=paginator.page(paginator.num_pages)
            
        
    return render(request, 'store.html', {'products':product})




def category_list(request): 
    
    queryset = ProductCategory.objects.all()
    
    return render(request, 'main.html', {'categorylist':queryset})




def product_view(request, slug_url, product_slug):
    try:
        prod = Product.objects.get(category__slug=slug_url, slug=product_slug)
        
    except Exception as e:
        raise e
    
    return render(request, "product_view.html", {'prod': prod})




def search(request):
    
    query = None
    result = None
    if "q" in request.GET:
        query = request.GET['q']
        result = Product.objects.all().filter(Q(product_name__icontains=query) | Q(product_desc__icontains=query))
    else:
        result = Product.objects.all()
        
    return render(request, "search.html", {'result': result, 'query': query})

