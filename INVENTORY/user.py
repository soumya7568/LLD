from cart import Cart

class User:
    def __init__(self,user_id, name, address):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.cart = Cart()
        self.orders = []
        