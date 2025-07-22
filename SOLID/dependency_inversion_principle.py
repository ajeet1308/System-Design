"""
Dependency Inversion Principle (DIP)

- High-level modules should not depend on low-level modules. Both should depend on abstractions.
- Abstractions should not depend on details. Details should depend on abstractions.
"""

from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def area(self):
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

class ShapePrinter:
    def print_shape(self, shape: IShape):
        print(shape.area())

shape_printer = ShapePrinter()
shape_printer.print_shape(Rectangle(10, 20))
shape_printer.print_shape(Square(10))
