'''
Requirements:

The system should create different shapes like Circle, Square, Triangle.

Each shape must have a draw() operation.

Adding a new shape (e.g., Hexagon) should not break or change existing client code.

'''

from abc import ABC, abstractmethod

#abstract class for different shapes
class Shape(ABC):
    @abstractmethod
    def draw():
        pass
    
#concrete shape class
class Circle(Shape):
    def draw(self):
        print("Drawing a circle......")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle......")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle......")


#shape factory
class ShapeFactory(ABC):
    @abstractmethod
    def get_shape():
        pass
    
class CircleFactory(ShapeFactory):
    def get_shape():
        return Circle()
    
class TriangleFactory(ShapeFactory):
    def get_shape():
        return Triangle()
    
class RectangleFactory(ShapeFactory):
    def get_shape():
        return Rectangle()
    
    
#client code
if __name__=="__main__":
    shape1 = CircleFactory.get_shape()
    shape1.draw()
    
    shape2= RectangleFactory.get_shape()
    shape2.draw()
    
    shape3 = TriangleFactory.get_shape()
    shape3.draw()
    

    
'''
Scalability:

Adding a new shape called hexagon:create shape for hexagon, create hexagon factory - no changes in code

'''




    