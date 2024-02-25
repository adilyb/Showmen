from django.shortcuts import render

# Create your views here.


def cart(request):
    return render(request, 'mainapp/cart.html')

def checkout(request):
    return render(request, 'mainapp/checkout.html')