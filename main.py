#--
#-- this program calculate the area of shapes
#--
from math import pi, pow
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type


    @abstractmethod
    def calculate_area(self):
        pass


class Circal(Shape):
    def __init__(self, radius):
        super().__init__("circale")
        self.radius = radius

    def calculate_area(self):
        return pi * pow(self.radius, 2)



class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        super().__init__("rectangle")
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        return super().calculate_area()
    
        
if __name__ == "__main__":
    # self test #
    c = Circal(2.5) 
    print(c.calculate_area())