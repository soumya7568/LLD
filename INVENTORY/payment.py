
class Payment:
    def __init__(self,payment_strategy):
        self.payment_strategy = payment_strategy
        
    def make_payment(self):
        return self.payment_strategy.make_payment()