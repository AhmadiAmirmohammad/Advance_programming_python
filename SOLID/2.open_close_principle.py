#This means you should be
# able to add new behavior without changing existing code.

# class DiscountCalculator: # محاسبه تخفیف
#     def calculate(self, customer_type, price):
#         if customer_type == "regular":
#             return price * 0.95
#         elif customer_type == "vip":
#             return price * 0.80
#         elif customer_type == "employee":
#             return price * 0.70

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class RegularDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.95

class VIPDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.80

class EmployeeDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.70

class BlackFridayDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.50

def discount_calculated(price, discount_strategy: DiscountStrategy):
    return discount_strategy.apply(price)

print(discount_calculated(1000, VIPDiscount()))          # 800.0
print(discount_calculated(1000, BlackFridayDiscount()))  # 500.0