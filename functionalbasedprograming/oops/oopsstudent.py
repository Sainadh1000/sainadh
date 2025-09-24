
class student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def info(self):    
        print("Name:",self.name)
        print("rollnumber",self.roll_number)
        print("marks",self.marks)
    def calculate_total(self):
        return sum(self.marks)
    def calculate_percentage(self):
        return sum(self.marks)/len(self.marks)
    def grade(self):
        percentage=self.calculate_percentage()
        if percentage>=80:
            return "A"
        elif percentage>=60:
            return "B"
        elif percentage>=40:
            return "C"
        else:
            return "F"

student_one=student("Venky",102,[89,90,97])   
student_one.info()
print("total:",student_one.calculate_total())
print("percentage:",student_one.calculate_percentage())
print("grade",student_one.grade())     