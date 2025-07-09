"""
Factory Pattern

The Factory Pattern is often used to hide the complexity of object creation from the client. It provides a level of abstraction, allowing the client to create objects without needing to know the specific class or how the object is instantiated. Instead, the client only interacts with the factory to obtain the desired object.

Use Case:
- When you need to create objects of different types based on some configuration or input.
- Hiding the complexity of object creation from the client.
- Providing a level of abstraction, allowing the client to create objects without needing to know the specific class or how the object is instantiated.
- Instead, the client only interacts with the factory to obtain the desired object.

Pros:
- Encapsulation: Hides the complexity of object creation from the client.
- Abstraction: Provides a level of abstraction, allowing the client to create objects without needing to know the specific class or how the object is instantiated.
- Extensibility: New product classes can be added without modifying existing code, promoting an open-closed principle.

Cons:
- Complexity: Introducing multiple Factory Methods and associated classes can lead to increased complexity.
- Abstraction Overhead: Creating numerous abstract classes and interfaces may add overhead to the codebase.
- Overkill: In simple scenarios, using the Factory Method pattern might be overkill and add unnecessary complexity.

"""

from abc import ABC, abstractmethod

# Interface
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

# Concrete Creator
class Car(Vehicle):
    # Concrete Product
    def drive(self):
        return "Driving a car"

class Truck(Vehicle):
    # Concrete Product
    def drive(self):
        return "Driving a truck"

# Creator
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError(f"Vehicle type {vehicle_type} not recognized.")

# Client
if __name__ == "__main__":
    vehicle_type = input("Enter the vehicle type (car/truck): ").lower()
    
    # Use the factory to create a vehicle
    vehicle = VehicleFactory.get_vehicle(vehicle_type)
    
    # Call the method on the created vehicle object
    print(vehicle.drive())

# Input: car
# Output: Driving a car

# Input: truck
# Output: Driving a truck

# Input: motorcycle
# Output: ValueError: Vehicle type motorcycle not recognized.
