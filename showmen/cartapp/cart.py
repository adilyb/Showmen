from mainapp.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        self.cart = cart
        
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        
        #logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
    def __len__(self):
        return len(self.cart)
    
    
    def get_prods(self):
        #get product ids from cart
        product_ids = self.cart.keys()
        #use ids to look up product from Database model
        products = Product.objects.filter(id__in = product_ids)
        #return those looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        
        #get cart
        
        ourcart  = self.cart
        ourcart[product_id] = product_qty
        
        self.session.modified = True
        
        thing = self.cart
        
        return thing
        
    