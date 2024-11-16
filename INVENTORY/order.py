from invoice import Invoice
from payment import Payment
from enums import OrderStatus

class Order:
    def __init__(self, user,warehouse):
        self.user = user
        self.products = user.cart.products
        self.address = user.address
        self.warehouse = warehouse
        self.status = OrderStatus.PENDING
        self.invoice = None
        
    def generate_invoice(self):
        total_cost = sum(product.price * quantity for product, quantity in self.products.items())
        self.invoice = Invoice(self,total_cost)
        return self.invoice
    
    def update_status(self,status):
        self.status = status
    
    def checkout(self):
        self.warehouse.upadte_product_quantity_in_inventory(self.products, False)
        is_payment_successful = self.make_payment()
        if is_payment_successful:
            self.user.cart.empty_cart()
            self.update_status(OrderStatus.SHIPPED)
            return self.generate_invoice()
        else:
            self.warehouse.upadte_product_quantity_in_inventory(self.products, True)
    
    def make_payment(self,payment_method):
        payment = Payment(payment_method)
        return payment.make_payment()  