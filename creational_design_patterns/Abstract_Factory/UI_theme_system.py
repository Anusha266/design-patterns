'''
Requirements:

The system should support two themes: Light Theme,Dark Theme

Each theme should provide two components:Button,Checkbox

Each component must have operations:

Button should have a render() method that shows whether it’s a Light or Dark button.

Checkbox should have a select() method that shows whether it’s a Light or Dark checkbox.

The system should allow switching between Light and Dark themes without changing existing code.

The system should be extensible:

If a new theme (e.g., High Contrast Theme) is introduced, it should be possible to add it without modifying the current implementation.
'''
from abc import ABC,abstractmethod

    
class Button(ABC):
    @abstractmethod
    def render():
        pass
    
class Checkbox():
    @abstractmethod
    def select(self):
        pass
    
    
class LightButton(Button):
    def render(self):
        print("rendering light button")
    
class DarkButton(Button):
    def render(self):
        print("rendering dark button")

class LightCheckbox(Checkbox):
    def select(self):
        print("Light checkbox selected")
        
class DarkCheckBox(Checkbox):
    def select(self):
        print("Dark checkbox selected")

class DarkButtonFactory():
    def get_theme():
        return DarkButton()
    
class LightButtonFactory():
    def get_theme():
        return LightButton()
    
class DarkCheckboxFactory():
    def get_theme():
        return DarkCheckBox()
    
   
class LightCheckboxFactory():
    def get_theme():
        return LightCheckbox()
    
#client code
if __name__=="__main__":
    DarkButtonFactory.get_theme().render()
    LightButtonFactory.get_theme().render()
    LightCheckboxFactory.get_theme().select()
    DarkCheckboxFactory.get_theme().select()



'''
Scalability:

For new theme: create new classes without changing existing code

learning:

class exploision because of combinations 
'''