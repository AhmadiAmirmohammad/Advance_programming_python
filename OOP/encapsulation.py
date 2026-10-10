#oop
#encapsulation
# 2 works:
    # encapsulate data (with private / protected)
    # provide access controlled way to read /write that data with getter/setter
from twisted.python.util import println
class CreditCard:
    def __init__(self, card_number, balance):
        self.__card_number = card_number  # private
        self.__balance = balance          # private
        self._daily_limit = 5000          # protected

    #getter in python
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance cannot be negative")
        self.__balance = value

    def pay(self, amount):
        if amount > self._daily_limit:
            raise ValueError("over daily limit")
        if amount > self.__balance:
            raise ValueError("balance not enough")
        self.__balance -= amount
        return f"task in done. {amount}"

    def __repr__(self):
        masked = "**** **** **** " + self.__card_number[-4:]
        return f"CreditCard({masked})"


card = CreditCard("1234567812345678", 2000)
println(card.pay(500))       #
println(card.balance)        #
card.balance = 3000        #
println(card)

#===============================================
#private
    # in class ✔
    # in child	❌
    # out of class	❌

#===============================================
#protected
    # in class ✔
    # in child ✔
    # out of class ✔ (Agreement (not used)
