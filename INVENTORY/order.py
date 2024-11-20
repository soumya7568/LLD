from invoice import Invoice
from payment import Payment
from enums import OrderStatus
from user import User
from warehouse import Warehouse
from payement_startegy import *

class Order:
    def __init__(self,oid, user:User,warehouse:Warehouse):
        self.order_id = oid
        self.user = user
        self.products = user.cart.products
        self.address = user.address
        self.warehouse = warehouse
        self.status = OrderStatus.PENDING
        self.invoice = None
        
    def generate_invoice(self):
        total_cost = 0
        for product_id, quantity in self.products.items():
            curr = self.warehouse.get_product_from_id(product_id)
            total_cost += curr.price * quantity
            
        self.invoice = Invoice(self.order_id,total_cost)
        return self.invoice.generate_invoice()
    
    def update_status(self,status):
        self.status = status
    
    def checkout(self):
        self.warehouse.upadte_product_quantity_in_inventory(self.products, False)
        is_payment_successful = self.make_payment(UPIPayment())
        if is_payment_successful:
            print("Payment successful")
            self.user.cart.empty_cart()
            self.update_status(OrderStatus.SHIPPED)
            return self.generate_invoice()
        else:
            print("Payment failed")
            self.warehouse.upadte_product_quantity_in_inventory(self.products, True)
            return "Order failed"
    
    def make_payment(self,payment_method):
        payment = Payment(payment_method)
        return payment.make_payment()  