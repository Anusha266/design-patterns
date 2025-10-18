""" 
Problem Statement: Coffee Shop Billing System

You are building a coffee shop billing system.

You have a base coffee (say, SimpleCoffee) that costs ₹50.

Customers can add extra ingredients like Milk, Sugar, or Whipped Cream, each increasing the cost and updating the description.

You want to design the system such that you can dynamically add any number of ingredients without modifying existing classes.
"""

from abc import ABC,abstractmethod

#=============component============
class Coffee(ABC):
    @abstractmethod 
    def cost(self):
        pass 

    @abstractmethod 
    def description(self):
        pass 


#concrete component 
class SimpleCoffee(Coffee):
    def cost(self):
        return 50 

    def description(self):
        return "Simple coffee "

#decorator base class on top of simple coffee
class CoffeeDecorator(Coffee):
    def __init__(self,coffee:Coffee):
        self._coffee=coffee

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass 

#concrete decorators============

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost()+10

    def description(self):
        return self._coffee.description()+"+ Milk"
    

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost()+5 

    def description(self):
        return self._coffee.description()+"+ Sugar"

class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost()+100 
    
    def description(self):
        return self._coffee.description()+"+ Whipped Cream"
    

    

#  Client Code
if __name__ == "__main__":
    # Base coffee
    coffee = SimpleCoffee()
    print(f"{coffee.description()} costs {coffee.cost()}")

    # Coffee with milk and sugar
    coffee_with_milk_sugar = SugarDecorator(MilkDecorator(SimpleCoffee()))
    print(f"{coffee_with_milk_sugar.description()} costs {coffee_with_milk_sugar.cost()}")

    # Coffee with whipped cream
    coffee_with_cream = WhippedCreamDecorator(SimpleCoffee())
    print(f"{coffee_with_cream.description()} costs {coffee_with_cream.cost()}")

    # Fully loaded coffee
    deluxe = WhippedCreamDecorator(SugarDecorator(MilkDecorator(SimpleCoffee())))
    print(f"{deluxe.description()} costs {deluxe.cost()}")