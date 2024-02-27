from .cart import Cart


#create context processors so our cart can work all pages
def cart(request):
    #return the default data from our cart
    return {'cart': Cart(request)}