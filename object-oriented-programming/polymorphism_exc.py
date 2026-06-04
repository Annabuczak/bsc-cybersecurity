class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print(f"Payment of £{self.amount} has been made/in progress.")


class CardPayment(Payment):
    def pay(self):
        print(f"Card payment of £{self.amount} has been made.")


class CashPayment(Payment):
    def pay(self):
        print(f"Cash payment of £{self.amount} has been made.")


class PayPalPayment(Payment):
    def pay(self):
        print(f"PayPal payment of £{self.amount} has been made.")


payments = [
    CardPayment(20),
    CashPayment(15),
    PayPalPayment(30)
]

for payment in payments:
    payment.pay()
