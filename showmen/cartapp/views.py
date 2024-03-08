from django.shortcuts import render, get_object_or_404
from .cart import Cart
from mainapp.models import Product
from django.http import JsonResponse
# Create your views here.


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    prod_quantities = cart.get_quants
    return render(request, 'cart.html', {"cart_products": cart_products, "prod_quantities": prod_quantities})

def add(request):
    #get the cart
    cart = Cart(request)
    
    #test for post
    if request.POST.get('action') == 'post':
        
        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
       
        #lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        
        #save to session
        cart.add(product=product, quantity=product_qty)
        
        cart_quantity = cart.__len__()
        
        #return response
        response = JsonResponse({'qty': cart_quantity})
        return response
    
        
def update(request):
    pass

def delete(request):
    pass

