# Create a class Animal with:

# attribute: name
# method: speak()

# Create a child class Dog that inherits from Animal and overrides speak() to print:


class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes a sound.")
class dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")
mydog=dog("Buddy")
mydog.speak()






# Task 2: Using super()

# Create a class Person:

# name
# age

# Create a child class Student with an additional attribute:

# grade

# Use super() to initialize parent attributes.

# Example:

# s = Student("John", 20, "A")

# Output:

# Name: John
# Age: 20
# Grade: A


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(person):
    def __init__(self,name,age,grade):
        super().__init__(name, age)
        self.grade=grade
    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

student1= student("sai","21","2year")
student1.details()


# Task 3: Employee Management

# Create a parent class:

# Employee

# Attributes:

# name
# salary

# Method:

# display_info()

# Create two child classes:

# Manager
# Developer

# Additional attributes:

# department
# programming_language

# Override display_info() in both classes.

# Expected Output:

# Manager: Alice
# Salary: 80000
# Department: HR

# Developer: Bob
# Salary: 70000
# Language: Python

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display_info(self):
        print(f"Manager: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"department: {self.department}")

class Developer(Employee):
    def __init__(self,name,salary,programing_language):
        super().__init__(name,salary)
        self.programing_language=programing_language
    def display_info(self):
        print(f"Developer: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"language: {self.programing_language}")

mymanager=Manager("Alice",80000,"HR")
mymanager.display_info()
mydeveloper=Developer("Bob",70000,"Python")
mydeveloper.display_info()




# Shape Area Calculator

# Create a base class:

# Shape

# Method:

# area()

# Create child classes:

# Rectangle
# Circle

# Implement area calculations.

# Example:

# Rectangle(5,4)
# Circle(3)

# Output:

# Rectangle Area = 20
# Circle Area = 28.27

import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape): 
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
rect = Rectangle(5, 4)
circle = Circle(3)

print(f"Rectangle Area (5x4): {rect.area()}")
print(f"Circle Area (r=3):    {circle.area():.2f}")




# Task 5: Vehicle System

# Create:

# Vehicle

# Attributes:

# brand
# model

# Method:

# display()

# Child classes:

# Car
# Bike

# Additional attributes:

# fuel_type
# engine_cc   

class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print("Use sub class for displaying any vehicle details") 
class car(vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type=fuel_type
    def display(self):
        print(f"car brand: {self.brand}")
        print(f"car model: {self.model}")
        print(f"car fuel type: {self.fuel_type}")

class bike(vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc=engine_cc
    def display(self):
        print(f"bike brand: {self.brand}")
        print(f"bike model: {self.model}")
        print(f"bike engine cc: {self.engine_cc}")
mybike=bike("passion pro","passion pro max","180 cc")
mybike.display()
mycar=car("benz","benz mount terrian ","desiel")
mycar.display()


# Task 6: Bank Account (Method Overriding)

# Parent:

# BankAccount

# Methods:

# deposit()
# withdraw()

# Child classes:

# SavingsAccount
# CurrentAccount

# Rules:

# Savings account cannot go below ₹1000.
# Current account can have overdraft up to ₹5000.

# Example:

# acc.withdraw(3000)

# Check whether transaction is allowed.



class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if self.balance >= amount:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Current Balance: ₹{self.balance}")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance}")


class SavingsAccount(BankAccount):
    MIN_BALANCE = 1000

    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)

        if balance < self.MIN_BALANCE:
            print("Warning: Savings Account should maintain at least ₹1000.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if self.balance - amount >= self.MIN_BALANCE:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Current Balance: ₹{self.balance}")
        else:
            print(
                f"Withdrawal denied! Savings Account must maintain ₹{self.MIN_BALANCE} minimum balance."
            )


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 5000

    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if self.balance + self.OVERDRAFT_LIMIT >= amount:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Current Balance: ₹{self.balance}")
        else:
            print(
                f"Withdrawal denied! Overdraft limit of ₹{self.OVERDRAFT_LIMIT} exceeded."
            )




print("===== Savings Account =====")

savings = SavingsAccount("Sai", 5000)

savings.show_balance()

savings.withdraw(3000)  

savings.withdraw(1500)  

savings.deposit(2000)

savings.show_balance()



print("\n===== Current Account =====")

current = CurrentAccount("John", 2000)

current.show_balance()

current.withdraw(6000)  
current.withdraw(2000) 

current.withdraw(2000) 

current.deposit(3000)

current.show_balance()






