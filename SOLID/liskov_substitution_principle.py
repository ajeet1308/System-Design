"""
Liskov Substitution Principle (LSP)

- The principle defines that objects of a superclass shall be replaceable with objects of its subclasses without breaking the application.
- That requires the objects of your subclasses to behave in the same way as the objects of your superclass.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class AreaCalculator:
    def calculate_area(self, shape):
        return shape.area()

rectangle = Rectangle(10, 20)
square = Square(10)

print(AreaCalculator().calculate_area(rectangle))
