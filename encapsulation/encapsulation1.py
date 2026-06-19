# Create a class Student.

# Requirements
# Private attribute: __marks
# Constructor should initialize marks.
# Method get_marks() returns the marks.
# Create an object and print the marks using the method.

class student:
    def __init__(self,marks):
        self.__marks=marks
    def set_marks(self,marks):
        if marks>=0:
            self.__marks=marks
        else:
            print("invalid marks")
    def get_marks(self):
        return self.__marks

s1=student(80)
s1.set_marks(80)
result=s1.get_marks()
print(result)


# Task 2: Getter and Setter

# Create a class BankAccount.

# Requirements
# Private attribute: __balance
# Constructor initializes balance.
# Method deposit(amount) adds money.
# Method withdraw(amount) subtracts money only if sufficient balance exists.
# Method get_balance() returns current balance.


class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def set_deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("invalid amount")
    def set_withdraw(self,amount):
        if amount>0 and self.__balance>amount:
            self.__balance-=amount
    def get_balance(self):
        return self.__balance
    
vamsi=BankAccount(10000)
vamsi.set_deposit(1000)
balance=vamsi.get_balance()
print(balance)
        
       
# Task 3: Validate Data with Setter

# Create a class Employee.

# Requirements
# Private attribute: __salary
# Method set_salary(salary)
# Salary cannot be negative.
# Method get_salary()
# Display an error message if an invalid salary is entered.

class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def set_salary(self,salary):
        if salary<0:
            print("salary cannot be negative")
        else:
            self.__salary=salary
    def get_salary(self):
        return self.__salary

emp1=Employee(100000)
emp1.set_salary(70000)
print(emp1.get_salary())


# Task 4: Password Protection

# Create a class User.

# Requirements
# Private attribute: __password
# Constructor initializes password.
# Method change_password(old_password, new_password)
# Change only if old password matches.
# Method verify_password(password) returns True or False.

class user:
    def __init__(self,password):
        self.__password=password
    def change_password(self,old_password,new_password):
        if old_password==self.__password:
            self.__password=new_password
            print(f"new password is {self.__password}")
        else:
            print("incorrect old password")
    def verify_password(self,password):
        return password==self.__password

a=user("user123")
a.change_password("user123","user456")


# Task 5: Product Inventory

# Create a class Product.

# Requirements
# Private attributes:
# __name
# __quantity
# Methods:
# add_stock(amount)
# sell(amount) (cannot sell more than available quantity)
# display_info()

# Expected Output

# Product: Laptop
# Quantity: 8

class product:
    def __init__(self,name,quantity):
        self.__name=name
        self.__quantity=quantity
    def add_stocks(self,amount):
        if amount>0:
            self.__quantity+=amount
            print(f"product: {self.__name}")
            print(f"quantity: {self.__quantity}")
        else:
            print("stock must be more than 0")
    def sell(self,amount):
        if amount>self.__quantity:
            print("products are not available")
        else:
            self.__quantity-=amount
            print(f"product: {self.__name}")
            print(f"quantity: {self.__quantity}")

shirt=product("lenin_shirt",100)
shirt.sell(90)
shirt.add_stocks(200)


# Task 6: Temperature Converter

# Create a class Temperature.

# Requirements
# Private attribute: __celsius
# Method set_temperature(temp)
# Temperature should not be below -273.15
# Method get_temperature()
# Method to_fahrenheit()


class temperature:
    def __init__(self,celsius):
        self.__celsius=celsius
    def set_temperature(self,temp):
        if temp< -273.15:
            print("Temperature should not be below -273.15")
        else:
            self.__celsius=temp
    def get_temperature(self):
        return self.__celsius
    def to_fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

t = temperature(25)
print(t.to_fahrenheit())


# Task 7: Library Management

# Create a class Book.

# Requirements
# Private attributes:
# __title
# __available
# Methods:
# borrow_book()
# return_book()
# check_status()

# Expected Output

# Book borrowed successfully.
# Book is not available.
# Book returned successfully.

class book:
    def __init__(self,title,available):
        self.__title=title
        self.__available=available
    def borrow_book(self):
        if self.__available.lower()=="yes":
            print("Book borrowed successfully.")
            self.__available="no"
        else:
            print("Book was not available.")
    def return_book(self):
        print("Book returned successfully.")
        self.__available="yes"
    def check_status(self):
        return self.__available

s1=book("mystery jungle","yes")
print(s1.check_status())
s1.borrow_book()
s1.return_book()
    
# Task 8: ATM Machine

# Create a class ATM.

# Requirements

# Private attributes:

# __pin
# __balance

# Methods:

# check_balance(pin)
# deposit(pin, amount)
# withdraw(pin, amount)
# Transactions should work only if the PIN is correct.

class ATM:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
    def check_balance(self,pin):
        if pin==self.__pin:
            print(f"available balance {self.__balance}")
        else:
            print("enter correct pin")
    def deposit(self,pin,amount):
        if pin==self.__pin and amount>0:
            self.__balance+=amount
            print(f"available balance {self.__balance}")
        elif amount<=0:
            print("amount must be greater than zero")
        else:
            print("enter correct pin")
    def withdraw(self,pin,amount):
        if pin==self.__pin and amount<=self.__balance:
            self.__balance-=amount
            print(f"available balance {self.__balance}")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            print("enter correct pin")

ac1=ATM(1234,2000)
ac1.check_balance(1342)
ac1.check_balance(1234)
ac1.deposit(1234,0)
ac1.deposit(1234,1000)
ac1.withdraw(1234,1000)



