# Create an abstract class Shape.

# Requirements
# Abstract method: area()
# Create subclasses:
# Rectangle
# Circle
# Each subclass should implement area().

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


shape1 = Rectangle(8, 9)
print(shape1.area())

shape2 = Circle(9)
print(shape2.area())



# Task 2: Animal Sounds

# Create an abstract class Animal.

# Requirements
# Abstract method: speak()
# Subclasses:
# Dog
# Cat
# Each should return its own sound.


class animal(ABC):
    @abstractmethod
    def speak(self):
        print("animal making sound")
    
class dog(animal):
    def speak(self):
        print("Woof!")
class cat(animal):
    def speak(self):
        print("Meow!")

animal1=dog()
animal1.speak()
animal2=cat()
animal2.speak()


# Task 3: Employee Salary

# Create an abstract class Employee.

# Requirements
# Abstract method: calculate_salary()
# Subclasses:
# FullTimeEmployee
# PartTimeEmployee

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class parttimeemployee(Employee):
    def __init__(self,time,amount):
        self.time=time
        self.amount=amount
    def calculate_salary(self):
        salary=self.time*self.amount
        print(f"total salary {salary}")
class fulltimeemployee(Employee):
    def __init__(self,amount):
        self.amount=amount
    def calculate_salary(self):
        print(f"total salary {self.amount}")

emp1=parttimeemployee(3,2000)
emp1.calculate_salary()
emp2=fulltimeemployee(50000)
emp2.calculate_salary()



# Task 4: Payment System

# Create an abstract class Payment.

# Requirements
# Abstract method: pay(amount)
# Subclasses:
# CreditCardPayment
# UPIPayment
# CashPayment

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class creditcardpayment(payment):
    def __init__(self,amount):
        self.amount=amount
    def pay(self):
        print(f"paid {self.amount} using credit card")
class upipayment(payment):
    def __init__(self,amount):
        self.amount=amount
    def pay(self):
        print(f"paid {self.amount} using upi")
class cashpayment(payment):
    def __init__(self,amount):
        self.amount=amount
    def pay(self):
        print(f"paid {self.amount} using cashpayment")

vamsi=creditcardpayment(10000)
vamsi.pay()


# Task 5: Vehicle Speed

# Create an abstract class Vehicle.

# Requirements
# Abstract method: max_speed()
# Subclasses:
# Car
# Bike
# Train

# Return different maximum speeds.    

class vehicle(ABC):
    @abstractmethod
    def max_speed(self):
        pass
class car(vehicle):
    def __init__(self,speed):
        self.speed=speed
    def max_speed(self):
        print(f"max speed of car is {self.speed} kmph")
class bike(vehicle):
    def __init__(self,speed):
        self.speed=speed
    def max_speed(self):
        print(f"max speed of bike is {self.speed} kmph")
class train(vehicle):
    def __init__(self,speed):
        self.speed=speed
    def max_speed(self):
        print(f"max speed of train is {self.speed} kmph")
veh1=car(90)
veh1.max_speed()
veh2=train(120)
veh2.max_speed()
veh3=bike(70)
veh3.max_speed()


# Requirements
# Abstract methods:
# connect()
# disconnect()

# Subclasses:

# MySQLDatabase
# MongoDatabase

class database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
class mysqldatabase(database):
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def connect(self):
        print(f"{self.username} is connected to mysqldatabase ")
    def disconnect(self):
        print(f"{self.username} is disconnected from mysqldatabase ")

class mangodatabase(database):
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def connect(self):
        print(f"{self.username} is connected to mangodatabase ")
    def disconnect(self):
        print(f"{self.username} is disconnected from mangodatabase ")
    
db1=mysqldatabase("sainadh",1234)
db1.connect()
db1.disconnect()
db2=mangodatabase("sainadh",12345)
db2.connect()
db2.disconnect()


# Task 7: Notification Service

# Create an abstract class Notification.

# Requirements
# Abstract method: send(message)

# Subclasses:

# EmailNotification
# SMSNotification
# PushNotification

class notification(ABC):
    @abstractmethod
    def send(self,message):
        pass
class EmailNotification(notification):
    def send(self,message):
        print(message)
class PushNotification(notification):
    def send(self,message):
        print(message)
class SMSNotification(notification):
    def send(self,message):
        print(message)
email=EmailNotification()
email.send("Welcome!")
sms=SMSNotification()
sms.send("OTP: 1234")


# Task 8: Banking System

# Create an abstract class Account.

# Requirements

# Abstract methods:

# deposit(amount)
# withdraw(amount)
# check_balance()

# Subclasses:

# SavingsAccount
# CurrentAccount

# Maintain separate balances.

class account(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def check_balance(self):
        pass
class savingsaccount(account):
    def __init__(self,balance):
        self.balance=balance
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"current balance {self.balance}")
        else:
            print("amount must be greater than zero")
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"current balance is {self.balance}")
        else:
            print("insuffiecient balance")
    def check_balance(self):
        print(f"current balance is {self.balance}")

class currentaccount(account):
    def __init__(self,balance):
        self.balance=balance
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"current balance {self.balance}")
        else:
            print("amount must be greater than zero")
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"current balance is {self.balance}")
        else:
            print("insuffiecient balance")
    def check_balance(self):
        print(f"current balance is {self.balance}")

acc1=savingsaccount(10000)
acc1.deposit(1000)   
acc1.withdraw(112000)
acc1.check_balance()
acc1.withdraw(2000)


# Task 9: Appliance Control

# Create an abstract class Appliance.

# Requirements

# Abstract methods:

# turn_on()
# turn_off()

# Subclasses:

# Fan
# AC
# WashingMachine

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class Fan(Appliance):
    def turn_on(self):
        print("Fan is switched on")
    def turn_off(self):
        print("fan switched off")
class AC(Appliance):
    def turn_on(self):
        print("AC is switched on")
    def turn_off(self):
        print("AC switched off")
class Washingmachine(Appliance):
    def turn_on(self):
        print("Washingmachine is switched on")
    def turn_off(self):
        print("Washingmachine switched off")
device1=Fan()
device1.turn_on()
device1.turn_off()
device2=Washingmachine()
device2.turn_on()
device2.turn_off()



# Task 10: Online Food Delivery

# Create an abstract class FoodOrder.

# Requirements

# Abstract methods:

# prepare()
# deliver()

# Subclasses:

# PizzaOrder
# BurgerOrder
# BiryaniOrder


class FoodOrder(ABC):
    @abstractmethod
    def prepare(self):
        pass
    @abstractmethod
    def deliver(self):
        pass
class PizzaOrder(FoodOrder):
    def prepare(self):
        print("Preparing Pizza")
    def deliver(self):
        print("Delivering Pizza")
class BurgerOrder(FoodOrder):
    def prepare(self):
        print("Preparing Burger")
    def deliver(self):
        print("Delivering Burger")
class BiriyaniOrder(FoodOrder):
    def prepare(self):
        print("Preparing Biriyani")
    def deliver(self):
        print("Delivering Biriyani")

order1=PizzaOrder()
order1.prepare()
order1.deliver()
order2=BiriyaniOrder()
order2.prepare()
order2.deliver()

    



