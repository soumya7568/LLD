from inventory import Inventory

class Warehouse():
    
    def __init__(self,address):
        self.inventory = Inventory()
        self.address = address
        
    def add_product_to_inventory(self, product):
        self.inventory.add_product(product)
        
    def remove_product_from_inventory(self, product):
        self.inventory.remove_product(product)
        
    def upadte_product_quantity_in_inventory(self, product_id_quantity_map,add=True):
        for product_id, quantity in product_id_quantity_map.items():
            self.inventory.update_quantity(product_id, quantity, add)
        