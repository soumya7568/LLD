from address import Address
from warehouse import Warehouse
from warehousecontroller import WarehouseController
from warehouse_selection_starategy import NearestWarehouseStrategy
from product import Product
from user import User 
from user_controller import UserController

class Main:
    
    def __init__(self):
        self.address = self.create_address()
        self.products = self.create_product()
        self.warehouse_controller = self.create_warehouse()
        self.users = self.create_user()
        self.order_excution()
    
    def create_address(self):
        address1 = Address("123 Main St", "New York", "NY", "10001")
        return [address1]
        
    
    def create_warehouse(self,count):
        self.warehouse_controller = WarehouseController(NearestWarehouseStrategy())
        for address in self.address:
            warehouse = Warehouse(address)
            self.warehouse_controller.add_warehouse(warehouse)
        
        for warehouse in self.warehouse_controller.warehouses.values():
            product_id_quantity_map = dict()
            for product in self.products:
                warehouse.add_product_to_inventory(product)
                product_id_quantity_map[product.product_id] = 10
            warehouse.upadte_product_quantity_in_inventory(product_id_quantity_map)
        
        return self.warehouse_controller
            
    def create_product(self):
        product1 = Product(1, "Product 1", 10)
        product2 = Product(2, "Product 2", 20)
        product3 = Product(3, "Product 3", 30)
        return [product1, product2, product3]
        
        
    def create_user(self):
        self.user_controller = UserController()
        user1 = User(1, "soumya", self.address[0])
        self.user_controller.add_user(user1)
        return [user1]
    
    def order_excution(self):
        user = self.user_controller.users["soumya"]
        warehouse = self.warehouse_controller.warehouses["10001"]