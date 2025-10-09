#Task 1: Vehicle Management System

#Create a base class Vehicle and two subclasses: Car and Motorcycle.

# Requirements:

# Class: Vehicle

# Attributes:

# brand (str)

# model (str)

# Method:

# start_engine() → prints: "Starting engine of <brand> <model>"

# Class: Car (inherits from Vehicle)

# Extra attribute:

# num_doors (int)

# Override start_engine() to print: "Car <brand> <model> with <num_doors> doors is starting."

# Class: Motorcycle (inherits from Vehicle)

# Extra attribute:

# type_of_bike (e.g., "Sport", "Cruiser")

# Override start_engine() to print: "Motorcycle <brand> <model> of type <type_of_bike> is starting."

# Create objects of both Car and Motorcycle, and call start_engine() on each.

class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def startengine(self):
        print(f"Starting engine of {self.brand} {self.model}")
class car(vehicle):
    def __init__(self, brand, model,num_doors):
        super().__init__(brand, model)
        self.num_doors=num_doors
    def startengine(self):
        print(f"car {self.brand} {self.model} with {self.num_doors} doors is starting")
class motorcycle(vehicle):
    def __init__(self, brand, model,type_of_bike):
        super().__init__(brand, model)
        self.type_of_bike=type_of_bike
    def startengine(self):
        print(f"motorcycle {self.brand} {self.model} of type {self.type_of_bike} is starting")