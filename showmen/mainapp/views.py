from django.shortcuts import render
from . models import Product
# Create your views here.


def store(request):
    prod = Product.objects.all()
    return render(request, 'mainapp/store.html', {'prod':prod})
