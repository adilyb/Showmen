from django.shortcuts import render, get_object_or_404
from .cart import Cart
from mainapp.models import Product
from django.http import JsonResponse
# Create your views here.


def cart(request):
    return render(request, 'cart.html', {})

def add(request):
    #get the cart
    cart = Cart(request)
    #test for post
    if request.POST.get('action') == 'post':
        
        #get stuff
        product_id = int(request.POST.get('product_id'))
        
       
        #lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        
        #save to session
        cart.add(product=product)
        
        cart_quantity = cart.__len__()
        
        #return response
        response = JsonResponse({'qty': cart_quantity})
        return response
        
def update(request):
    pass

def delete(request):
    pass

