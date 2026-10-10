#A class can inherit the properties and behaviors of another class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} voice creator"


class Dog(Animal):
    def speak(self):
        return f"{self.name} vagh vagh"


class Cat(Animal):
    def speak(self):
        return f"{self.name} miu miu"

d = Dog("reks")
print(d.speak())  #