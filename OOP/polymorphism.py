#Base of object, a method with same name can be various behavior

class PaymentMethod:
    def process(self, amount):
        raise NotImplementedError("sould be implemented in child class")

class PayPal(PaymentMethod):
    def process(self, amount):
        return f"pay as PayPal {amount}"

class CryditCardPayment(PaymentMethod):
    def process(self, amount):
        return f"pay as Crydit Card{amount}"

class CryptoPayment(PaymentMethod):
    def process(self, amount):
        return f"pay as  Crypto Payment {amount} "

def checkout(payment_method: PaymentMethod, amount):
    print(payment_method.process(amount))

methods = [PayPal(), CryditCardPayment(), CryptoPayment()]
for method in methods:
    checkout(method, 100)