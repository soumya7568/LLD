from address import Address
from warehouse import Warehouse
from product import Product
from user import User 
from Inventory_app import InventoryApp

class Main:
    
    def __init__(self):
        self.address = self.create_address()
        self.products = self.create_product()
        self.warehouse_array = self.create_warehouse()
        self.users = self.create_user()
        self.inventory_app = InventoryApp()
        self.start_the_app()
    
    def create_address(self):
        address1 = Address("123 Main St", "New York", "NY", "10001")
        return [address1]
        
    
    def create_warehouse(self):
        warehouse_array = []
        for address in self.address:
            warehouse = Warehouse(address)
            warehouse_array.append(warehouse)
        
        for warehouse in warehouse_array:
            product_id_quantity_map = dict()
            for product in self.products:
                warehouse.add_product_to_inventory(product)
                product_id_quantity_map[product.product_id] = 10
            warehouse.upadte_product_quantity_in_inventory(product_id_quantity_map)
        
        return warehouse_array
            
    def create_product(self):
        product1 = Product(1, "Coke", 10)
        product2 = Product(2, "Cake", 20)
        product3 = Product(3, "Ganja", 30)
        return [product1, product2, product3]
        
        
    def create_user(self):
        user1 = User(1, "soumya", self.address[0])
        return [user1]
        
    def start_the_app(self):
        for user in self.users:
            self.inventory_app.user_controller.add_user(user)
        
        for warehouse in self.warehouse_array:
            self.inventory_app.warehouse_controller.add_warehouse(warehouse)
            
        user = self.inventory_app.user_controller.users["soumya"]
        warehouse = self.inventory_app.warehouse_controller.select_warehouse()
        
        inventory = self.inventory_app.get_the_inventory(warehouse)
        
        all_products = self.inventory_app.show_all_inventory_products(inventory)
        
        for product_id,product in all_products.items():
            if product.name.lower()=="ganja":
                self.inventory_app.add_item_to_cart(user,product,5)
                break
            
        order = self.inventory_app.place_order(user,warehouse)
        
        order_status =self.inventory_app.checkout_order(order)
        print(order_status)
            
        