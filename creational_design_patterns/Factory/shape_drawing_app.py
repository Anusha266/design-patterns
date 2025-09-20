'''
Requirements:

The system should create different shapes like Circle, Square, Triangle.

Each shape must have a draw() operation.

A factory should decide which shape object to return based on input.

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
class ShapeFactoryInterface(ABC):
    @abstractmethod
    def get_shape(shape):
        pass
    
#shapeFactory
class ShapeFactory(ShapeFactoryInterface):
    _shapes={
        'circle':Circle,
        'triangle':Triangle,
        'rectangle':Rectangle
    }
    @staticmethod
    def get_shape(shape):
        try:
            return ShapeFactory._shapes[shape]()
        except KeyError:
            raise ValueError("Unknown shape:",shape)
        
        
#client code
if __name__=="__main__":
    shape1 = ShapeFactory.get_shape("circle")
    shape1.draw()
    
    shape2= ShapeFactory.get_shape("rectangle")
    shape2.draw()
    
    shape3 = ShapeFactory.get_shape("triangle")
    shape3.draw()
    
    Shape_unknown = ShapeFactory.get_shape("hexagon")
    Shape_unknown.draw()
    
    
'''
Learnings: 
1.factory is stateless so we can't pass shape first and store. Better to declare method as static method and call directly.
2. maintaining in  a map for classes instead of if else in factory
Key Learning Recap

3. Factory returns objects, not strings.  ( for unknown shape -> returned a string "not a valid shape")

4. Current design still violates OCP , solved with dictionary. (initially if else conditions used for each shape)

scalability:

Add hexagon shape:
add another shape class hexagon. 
modify factory to accept hexagon. (so here solid principle(open/closed) fails - no modification of existing class) - abstract factory used to solve this

'''
    
    




    