from warehouse import Warehouse
from warehousecontroller import WarehouseController
from warehouse_selection_starategy import NearestWarehouseStrategy
from product import Product
from user import User 
from user_controller import UserController
from ordercontroller import OrderController
from warehouse import Warehouse
from inventory import Inventory
from order import Order



class InventoryApp:
    def __init__(self):
        self.warehouse_controller = WarehouseController(NearestWarehouseStrategy())
        self.user_controller = UserController()
        self.order_controller = OrderController()
        
        
    def get_the_inventory(self,warehouse : Warehouse):
        return warehouse.inventory
        
    def show_all_inventory_products(self,inventory:Inventory):
        return inventory.show_all_products()
    
    def add_item_to_cart(self,user:User,product:Product,count):
        cart = user.cart
        cart.add_product(product,count)
        
    def place_order(self,user:User,warehouse:Warehouse):
        return self.order_controller.create_order(user,warehouse)
    
    def checkout_order(self,order:Order):
        return order.checkout()