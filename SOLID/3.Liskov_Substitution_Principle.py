#If class B is a child of class A,
# it should be possible to replace B
# wherever A is used without breaking the program's behavior.

#This means that Square cannot properly replace Rectangle — a violation of LSP,
# even though mathematically a square is a special type of rectangle.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Rectangle(5, 10), Square(5)]
for s in shapes:
    print(s.area()) 