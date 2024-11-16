from abc import ABC,abstractmethod

class PaymentStaregy(ABC):
    @abstractmethod
    def make_payment(self,order):
        pass
    
class UPIPayment(PaymentStaregy):
    def make_payment(self,order):
        pass
    
class CreditCardPayment(PaymentStaregy):
    def make_payment(self,order):
        pass