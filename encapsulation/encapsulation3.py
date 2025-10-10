# Create a class named Student.

# Add private attributes:

# name (string)

# age (int)

# grade (float)

# Provide public methods to:

# Set the student's details (set_name, set_age, set_grade)

# Get each detail (get_name, get_age, get_grade)

# Add a method to display the student’s full information.

class student:
    def __init__(self,name,age,grade):
        self.__name=name
        self.__age=age
        self.__grade=grade
    def set_name(self,name):
        if name:
            self.__name=name
        else:
            print("name invalid")
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("age invalid")
    def set_grade(self,grade):
        if grade>0:
            self.__grade=grade
        else:
            print("grade invalid")
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_grade(self):
        return self.__grade

    def display_info(self):
        print("Student Name:", self.__name)
        print("Age:", self.__age)
        print("Grade:", self.__grade)
a=student("Alice", 17, 89.5)
a.display_info()
a.set_name('sai')
a.set_grade(98.09)
a.set_age(20)
a.display_info()