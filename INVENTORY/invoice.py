class Invoice:
    def __init__(self, order, total_cost):
        self.order = order
        self.total_cost = total_cost
        self.total_tax = total_cost * 0.1
        self.total_cost_with_tax = total_cost + self.total_tax
        
    def generate_invoice(self):
        return f"Order ID: {self.order.order_id}\nTotal Cost: {self.total_cost}\nTotal Tax: {self.total_tax}\nTotal Cost with Tax: {self.total_cost_with_tax}"