from product import Product
from collections import defaultdict

class Inventory:
    def __init__(self):
        self.id_product_map = dict()
        self.product_id_quantity_map = defaultdict(int)
        
    def add_product(self, product:Product):
        self.id_product_map[product.product_id] = product
        
    def remove_product(self, product:Product):
        del self.id_product_map[product.product_id]
        
    def get_product(self, product_id):
        return self.id_product_map[product_id]
    
    def update_quantity(self, product_id, quantity, add=True):
        if add:
            self.product_id_quantity_map[product_id] += quantity
        else:
            self.product_id_quantity_map[product_id] -= quantity
        return self.product_id_quantity_map[product_id]
    
    def show_all_products(self):
        return self.id_product_map