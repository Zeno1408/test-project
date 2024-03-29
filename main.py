
from math import pi 
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> None:
        pass

class Square(Shape):
    def __init__(self, side: int | float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2
    
class Circle(Shape):
    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

area_square = Square(2).area()
area_circle = Circle(2).area()

print(f"Square Area: {area_square} sq.unit")
print(f"Circle Area: {area_circle} sq.unit")