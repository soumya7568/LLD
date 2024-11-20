from abc import ABC,abstractmethod

class PaymentStaregy(ABC):
    @abstractmethod
    def make_payment(self):
        return True
    
class UPIPayment(PaymentStaregy):
    def make_payment(self):
        return True
    
class CreditCardPayment(PaymentStaregy):
    def make_payment(self):
        return True