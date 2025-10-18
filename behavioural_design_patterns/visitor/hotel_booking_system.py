"""
Problem Statement:
You are managing a hotel that has Single Rooms and Double Rooms.
Each type of room can have different operations, such as:

Calculating Room Price

Calculating Maintenance Cost

You want to add new operations in the future (like cleaning cost or discount calculation) without modifying the Room classes.
"""

#each operation is isolated - using double dispatch

from abc import ABC, abstractmethod

# Visitor interface
class IVisitor(ABC):
    @abstractmethod
    def visit_single_room(self, room):
        pass

    @abstractmethod
    def visit_double_room(self, room):
        pass


# Element interface
class IElement(ABC):
    @abstractmethod
    def accept(self, visitor: IVisitor):
        pass


# Concrete elements
class SingleRoom(IElement):
    def __init__(self, room_number):
        self.room_number = room_number

    def accept(self, visitor: IVisitor):
        return visitor.visit_single_room(self)


class DoubleRoom(IElement):
    def __init__(self, room_number):
        self.room_number = room_number

    def accept(self, visitor: IVisitor):
        return visitor.visit_double_room(self)


# Concrete Visitors
class RoomPriceVisitor(IVisitor):
    def visit_single_room(self, room: SingleRoom):
        print(f"Price for single room {room.room_number} is: 2000")

    def visit_double_room(self, room: DoubleRoom):
        print(f"Price for double room {room.room_number} is: 4000")


class RoomMaintenanceVisitor(IVisitor):
    def visit_single_room(self, room: SingleRoom):
        print(f"Maintenance cost for single room {room.room_number} is: 1000")

    def visit_double_room(self, room: DoubleRoom):
        print(f"Maintenance cost for double room {room.room_number} is: 2000")


#client code 
if __name__ == "__main__":
    rooms = [SingleRoom(101), DoubleRoom(202), SingleRoom(103)]

    price_visitor = RoomPriceVisitor()
    maintenance_visitor = RoomMaintenanceVisitor()

    print("=== Room Prices ===")
    for room in rooms:
        room.accept(price_visitor)

    print("\n=== Maintenance Costs ===")
    for room in rooms:
        room.accept(maintenance_visitor)
