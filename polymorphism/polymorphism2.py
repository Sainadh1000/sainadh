# Create a base class PaymentMethod:

# Method: process_payment(amount) → just print a generic message.

# Create three subclasses, each overriding process_payment(amount):

# CreditCardPayment

# Print: "Processing credit card payment of $<amount>"

# PayPalPayment

# Print: "Processing PayPal payment of $<amount>"

# BankTransferPayment

# Print: "Processing bank transfer payment of $<amount>"

# Create a function make_payment(payment_method, amount) that takes a PaymentMethod object and an amount, and calls process_payment().

# Create a list of different payment method objects and simulate payments of varying amounts using a loop and make_payment().

class paymentmethod:
    def process_payment(self,amount):
        print("available balance",amount)
class creditcardpayment(paymentmethod):
    def process_payment(self,amount):
        fee = self.get_transaction_fee(amount)
        print(f"Processing creditcard payment of {amount} with transaction fee {fee}")
    def get_transaction_fee(self, amount):
        return amount * 0.01
class paypalpayment(paymentmethod):
    def process_payment(self,amount):
        fee = self.get_transaction_fee(amount)
        print(f"Processing paypal payment of {amount} with transaction fee {fee}")
    def get_transaction_fee(self, amount):
        return amount * 0.02
class banktransferpayment(paymentmethod):
    def process_payment(self,amount):
        fee = self.get_transaction_fee(amount)
        print(f"Processing bank transfer payment of {amount} with transaction fee {fee}")
    def get_transaction_fee(self, amount):
        return amount * 0.03

sai=[creditcardpayment(),paypalpayment(),banktransferpayment()]
for i in sai:
    i.process_payment(200)