# Task 1: Basic Method Overriding (Inheritance-Based)Goal: Learn how a child class overrides a parent 
# class method.
# Scenario: Create a base class named Vehicle with a method start_engine() that returns "Engine started."
# Subclasses: Create two child classes, Car and ElectricCar, that inherit from Vehicle.
# Requirement: Override start_engine() in Car to return "Vroom! Gas engine is roaring."
# Override it in ElectricCar to return "Silent hum... Electric motor is ready." \
# ""Execution: Write a function test_vehicle(vehicle_obj) that accepts any vehicle
# and prints the output of its engine status without checking its specific class type.



class Vehicle:
    def start_engine(self):
        print("engine started")
class car(Vehicle):
      def start_engine(self):
        print("Vroom! Gas engine is roaring.")
class ElectricCar(Vehicle):
      def start_engine(self):
        print("Silent hum... Electric motor is ready." )
def test_vehicle(vechicle_list):
    for vehicle_obj in vechicle_list:
        vehicle_obj.start_engine()
Vehicles=[car(),ElectricCar()]
test_vehicle(Vehicles)




# Task 2: Duck Typing (Interface-Based Polymorphism)
# In Python, you don't always need inheritance to achieve polymorphism. Python uses "Duck Typing"—if it walks like a duck and quacks like a duck, it's a duck.

# Scenario
# You are building a notification manager. Different services send messages in different ways, but they all should be able to "send".

# Requirements
# Create a SMS class with a method send(self, message) that prints: f"Sending SMS: {message}".

# Create a Email class with a method send(self, message) that prints: f"Sending Email: {message}".

# Crucial: Do not use a parent class. These classes should be entirely independent.

# Write a function broadcast_alert(notification_objects, message) that takes a list of different notification objects and loops through them to send the message.

class sms:
    def send(self,message):
        print(f"sending SMS: {message}")
class email:
    def send(self,message):
        print(f"sending Email: {message}")
    
def broadcast_alert(notification_list,message):
    for notification_obj in notification_list:
        notification_obj.send(message)

service=[email(),sms()]
broadcast_alert(service,"System update")


# Task 3: Operator Overloading (Magic Methods)
# Polymorphism also applies to operators (like +, -, *). For example, + adds two numbers, but it also concatenates two strings. You can make + do custom things for your own classes using "magic methods".

# Scenario
# You are managing a bank budget and want to easily add custom Wallet objects together.

# Requirements
# Create a class Wallet that takes cash (an integer/float) in its __init__.

# Override the magic method __add__(self, other) so that when you write wallet1 + wallet2, it returns a new Wallet object containing the combined cash of both.

# Override the __str__(self) magic method so that printing a wallet object displays: f"Wallet with ${self.cash}".

class wallet:
    def __init__(self,cash):
        self.cash=cash
    def __add__(self,other):
        return wallet(self.cash + other.cash)
    def __str__(self):
        return f"wallet with ${self.cash}"

wallet1 = wallet(100)
wallet2 = wallet(250)
wallet3 = wallet1 + wallet2
print(wallet1)
print(wallet2)
print(wallet3)


# Task : Employee Bonus Calculator

# Create a class Employee with a method calculate_bonus().

# Create child classes:

# Manager
# Developer
# Intern

# Each should calculate bonus differently.

# Example:

# Manager Bonus: 10000
# Developer Bonus: 5000
# Intern Bonus: 1000
    
class employee:
    def bonus(self):
        print("enter your designation to get bounus")
class manager(employee):
    def bonus(self):
        print("manager: 10000")
class developer(employee):
    def bonus(self):
        print("developer: 5000")
class intern(employee):
    def bonus(self):
        print("intern : 1000")
def designation_bonus(designation_list):
    for designation in designation_list:
        designation.bonus()
designations=[manager(),developer(),intern()]
designation_bonus(designations)


# Task 3: Shape Area

# Create a parent class Shape with method area().

# Create:

# Rectangle
# Circle
# Triangle

# Override area() for each shape.

# Example:

# Rectangle Area: 50
# Circle Area: 78.5
# Triangle Area: 25

class Shape:
    def area(self):
        print("enter your shapes to get area")
class rectangle(Shape):
    def area(self):
        print("rectangle: 50")
class circle(Shape):
    def area(self):
        print("circle: 78.5")
class triangle(Shape):
     def area(self):
        print("triangle: 25")
def shapes_area(shapes_list):
    for shapes in shapes_list:
        shapes.area()
shapes_list=[rectangle(),triangle(),circle()]
shapes_area(shapes_list)
