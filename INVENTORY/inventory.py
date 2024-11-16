class Inventory:
    def __init__(self):
        self.id_product_map = dict()
        self.product_id_quantity_map = dict()
        
    def add_product(self, product):
        self.id_product_map[product.product_id] = product
        
    def remove_product(self, product):
        del self.id_product_map[product.product_id]
        
    def get_product(self, product_id):
        return self.id_product_map[product_id]
    
    def update_quantity(self, product_id, quantity, add=True):
        if add:
            self.product_id_quantity_map[product_id] += quantity
        else:
            self.product_id_quantity_map[product_id] -= quantity
        return self.product_id_quantity_map[product_id]