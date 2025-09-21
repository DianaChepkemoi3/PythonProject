import math
import sys


class Circle:

    units='cm'
    def __init__(self,radius,fill="white",stroke="black",position=(0,0)):
        self.radius=radius
        self.position=position
        self.fill=fill
        self.stroke=stroke

        self.diameter= 2 * radius

        def __str__(self):
            return f"I am a circle of size{self.radius}{self.units} located at{self.position}."

        def area(self):
            return math.pi * self.radius ** 2

        def perimeter(self):
            return 2 * math.pi * self.radius
