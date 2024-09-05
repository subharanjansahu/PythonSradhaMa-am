'''
Define a cricle class to create a cricle with radius r using the constructor.
Define an Area() method of the class which calculate the area of circle.
Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
'''

from math import pi

class Circle:
  def __init__(self,redius) -> None:
    self.redius = redius
  
  def Area(self):
    return pi*(self.redius ** 2)
  
  def Perimeter(self):
    print('Perimeter is :',2 * pi * self.redius)
  
c = Circle(3)
print('Area is :',c.Area())
c.Perimeter()