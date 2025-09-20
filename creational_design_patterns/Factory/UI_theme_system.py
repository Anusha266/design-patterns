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
    def render():
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

class ThemeFactory():
    @staticmethod
    def get_component_theme(component,theme):
        if component=='button':
            if theme=='dark':
                return DarkButton()
            elif theme=='light':
                return LightButton()
        elif component == 'checkbox':
            if theme=='dark':
                return DarkCheckBox()
            elif theme=='light':
                return LightCheckbox()
               
#client code
if __name__=="__main__":
    ThemeFactory.get_component_theme('button','dark').render()
    ThemeFactory.get_component_theme('button','light').render()
    ThemeFactory.get_component_theme('checkbox','dark').select()
    ThemeFactory.get_component_theme('checkbox','light').select()



'''
Scalability:

For new theme: open/closed principle violates
'''