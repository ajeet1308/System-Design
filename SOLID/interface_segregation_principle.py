"""
Interface Segregation Principle (ISP)

- Clients should not be forced to depend on interfaces they do not use.
- It’s better to have multiple smaller, specific interfaces than a large, general-purpose one.
"""
from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def area(self):
        pass

class IAreaCalculator(ABC):
    @abstractmethod
    def calculate_area(self, shape):
        pass

class Rectangle(IShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(IShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class AreaCalculator(IAreaCalculator):
    def calculate_area(self, shape):
        return shape.area()

rectangle = Rectangle(10, 20)
square = Square(10)

print(AreaCalculator().calculate_area(rectangle))
print(AreaCalculator().calculate_area(square))
