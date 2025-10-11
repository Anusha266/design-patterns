'''
Problem:
You are building a shopping application. Users can pay using multiple payment methods: Credit Card, UPI, or Cash.
Implement a system where the payment method can be chosen and changed at runtime without modifying the main shopping class.
'''
from abc import ABC,abstractmethod

#abstract interface for payment
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass

#concrete classes
class CreditCardStrategy(PaymentStrategy): #is -a relation with payment-strategy
    def pay(self):
        print("paying through credit card...........")
    

class UPIStrategy(PaymentStrategy):
    def pay(self):
        print("paying through UPI..........")

class CashStrategy(PaymentStrategy):
    def pay(self):
        print("paying through cash.........")

#main class
class Shopping():
    def __init__(self,payment:PaymentStrategy):
        self.payment = payment # has -a relation with PaymentStrategy type 
    def pay(self):
        self.payment.pay()

if __name__=="__main__":
    Shop = Shopping(CreditCardStrategy()).pay() 
    Sho = Shopping(UPIStrategy()).pay() 
    Shop = Shopping(CashStrategy()).pay() 
    

