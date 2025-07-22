"""
Open/Closed Principle (OCP)

- A class should be open for extension but closed for modification.
- We should be able to extend the behavior of a class without modifying it. 
"""

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)

class AreaCalculator:
    def calculate_area(self, shape):
        return shape.area()

rectangle = Rectangle(10, 20)
square = Square(10)
circle = Circle(10)

area_calculator = AreaCalculator()
print(area_calculator.calculate_area(rectangle))
print(area_calculator.calculate_area(square))
print(area_calculator.calculate_area(circle))
