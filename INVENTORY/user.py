from cart import Cart
from address import Address

class User:
    def __init__(self,user_id, name, address:Address):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.cart = Cart()
        self.orders = []
        