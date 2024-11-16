class Cart:
    def __init__(self):
        self.products = dict()
        
    def add_product(self, product, quantity):
        self.products[product.product_id] = quantity
    
    def remove_product(self, product,quantity):
        self.products[product.product_id] -= quantity
        if self.products[product.product_id] == 0:
            del self.products[product.product_id]
            
    def view_cart(self):
        return self.products
        
    def empty_cart(self):
        self.products = {}