print("This is OOP Practice Exercise 1 Script")
import math


class Line():

    def __init__(self,coord1,coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        x1 = self.coord1[0]
        x2 = self.coord2[0]

        y1 = self.coord1[1]
        y2 = self.coord2[1]

        dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return dis

    def slope(self):
        x1 = self.coord1[0]
        x2 = self.coord2[0]

        y1 = self.coord1[1]
        y2 = self.coord2[1]

        sl = (y2-y1)/(x2-x1)
        return sl



class Cylinder():

    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = self.pi * self.radius**2 * self.height
        return vol

    def surface_area(self):
        area = 2 * self.pi * self.radius * (self.height + self.radius)
        return area

#  ----------------------------------------------------

coordinate1 = (3,2)
coordinate2 = (8,10)

my_line = Line(coordinate1,coordinate2)
print(my_line.slope())
print(my_line.distance())

my_cylinder = Cylinder(2,3)
print(my_cylinder.surface_area())
print(my_cylinder.volume())