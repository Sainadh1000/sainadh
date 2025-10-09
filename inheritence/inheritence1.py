class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, student_id, grades):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = grades

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def show_info(self):
        avg_grade = self.get_average_grade()
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Average Grade: {avg_grade:.2f}")

# Subclass: Teacher
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Subject: {self.subject}")

# Example usage
person = Person("Alice", 40)
student = Student("Bob", 16, "S123", [85, 90, 78])
teacher = Teacher("Mr. Smith", 45, "T456", "Mathematics")

person.show_info()
student.show_info()
teacher.show_info()