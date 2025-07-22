"""
Single Responsibility Principle (SRP)

- A class should have only one reason to change, meaning it should have only one job or responsibility.
 
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

rectangle = Rectangle(10, 20)
print(rectangle.area())

square = Square(10)
print(square.area())
