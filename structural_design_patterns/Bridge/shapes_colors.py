


'''
#######without bridge pattern ########################

Shape
 ├── Circle (Red)
 ├── Circle (Blue)
 ├── Square (Red)
 └── Square (Blue)


 Here shape and color both are tightly coupled.. Adding new shape or color leads to class explosion.

'''


############### WIth BRIDGE pattern##########################
#Decouples an abstraction from its implementation, so the two can vary independently.


# Implementor
class Color:
    def apply_color(self):
        pass

# Concrete Implementors
class RedColor(Color):
    def apply_color(self):
        return "Red"
    
class BlueColor(Color):
    def apply_color(self):
        return "Blue"
    

# Abstraction
class Shape:
    def __init__(self, color: Color):
        self.color = color # Shape (has-a) color

    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print(f"Drawing Circle in {self.color.apply_color()} color")

class Square(Shape):
    def draw(self):
        print(f"Drawing Square in {self.color.apply_color()} color")





# ---- Client code ----
red = RedColor()
blue = BlueColor()

circle1 = Circle(red)
circle2 = Circle(blue)
square1 = Square(red)

circle1.draw()   # Drawing Circle in Red color
circle2.draw()   # Drawing Circle in Blue color
square1.draw()   # Drawing Square in Red color










