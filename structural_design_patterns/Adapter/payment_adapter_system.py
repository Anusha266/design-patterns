"""
Problem Statement

Your application expects all payments to be processed using a method process_payment(amount).
However, third-party gateways (like PayPal, Stripe) have different method names and parameter formats.

"""

from abc import ABC,abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(amount):
        pass
        print(f" Transaction successful for {amount}")

#third party payment systems
class Stripe:
    def make_charge(sef,value):
        print("Stripe processed payment of",value)


class Paypal:
    def send_payment(self,value):
        print("paypal processed payment of ",value)

    
#adapters for each payment method
class StripeAdapter(PaymentProcessor):
    def __init__(self,stripe:Stripe):
        self.stripe=stripe

    def process_payment(self,amount):
        self.stripe.make_charge(amount)

class PaypalAdapter(PaymentProcessor):
    def __init__(self,paypal:Paypal):
        self.paypal=paypal
    def process_payment(self,amount):
        self.paypal.send_payment(amount)


# Client code
def complete_purchase(processor:PaymentProcessor,amount):
    processor.process_payment(amount)


# Usage
paypal_adapter = PaypalAdapter(Paypal())
stripe_adapter = StripeAdapter(Stripe())

complete_purchase(paypal_adapter, 2500)
complete_purchase(stripe_adapter, 4000)