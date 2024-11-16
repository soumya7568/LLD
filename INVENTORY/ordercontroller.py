from collections import defaultdict
from order import Order
class OrderController:
    def __init__(self):
        self.orders = dict()
        self.userid_order_map = defaultdict(list)
        self.order_count = 0
        
    def create_order(self, user,warehouse):
        self.order_count += 1
        new_order = Order(user,warehouse)
        self.orders[self.order_count] = new_order
        self.userid_order_map[user.user_id].append(new_order)
        return new_order
    
    def get_order_by_user_id(self, user_id):
        return self.userid_order_map[user_id]