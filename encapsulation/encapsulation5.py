#  Create a class Employee with the following private attributes:

# __name (string)

# __employee_id (int)

# __salary (float)

#  Create methods to:

# Set values (with validation):

# set_name(name) – must be non-empty

# set_employee_id(emp_id) – must be a positive integer

# set_salary(salary) – must be a non-negative number

# Get values:

# get_name()

# get_employee_id()

# get_salary()

# Display employee info:

# display_info() – print all details

# Give raise:

# Method give_raise(percent) that increases salary by a given percentage

class employee:
    def __init__(self,name,employee_id,salary):
        self.__name=name
        self.__employee_id=employee_id
        self.__salary=salary
    def set_name(self,name):
        if name:
            self.__name=name
        else:
            print("invalid")
    def set_employeeid(self,employee_id):
        if employee_id>0:
            self.__employee_id=employee_id
        else:
            print("invalid id")
    def set_salary(self,salary):
        if salary>=0:
            self.__salary=salary
        else:
            print("inavalid salary")
    def get_name(self):
        return self.__name
    def get_employeeid(self):
        return self.__employee_id
    def get_salary(self):
        return self.__salary
    def display_info(self):
        print(self.__name)
        print(self.__employee_id)
        print(self.__salary)
    def give_raise(self,percentage): 
        if percentage>0:
            self.__salary+=self.__salary*percentage/100 
            print(f"your salary is  increased by {percentage}% now new salary is {self.__salary}")
        else:
            print("no increment")
          
                  
a=employee("vamsi",2,20000)
a.display_info()
a.give_raise(2)
a.display_info()
