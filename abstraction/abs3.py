# Create an abstract class called Shape.

# Add an abstract method area().

# Create two subclasses: Rectangle and Circle.

# Each subclass should implement the area() method.

# Use appropriate formulas:

# Rectangle area = length * width

# Circle area = π * radius^2 (use math.pi)

# Create instances of both shapes and print their areas.

from abc import ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    
circle1=Circle(4)
print("area of circle1:",circle1.area())
Rectangle1=Rectangle(2,4)
print("area of rectangle1:",Rectangle1.area())

circle2=Circle(10)
print("area of circle2:",circle2.area())
Rectangle2=Rectangle(10,8)
print("area of rectangle2:",Rectangle2.area())

