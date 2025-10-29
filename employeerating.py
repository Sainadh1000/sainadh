# Task: Employee Performance Evaluation System
# 🧩 Requirements

# Write a Python program that:

# Takes employee details:

# Employee ID (must be digits only)

# Employee Name

# Accepts monthly performance ratings for multiple months (0–10 scale).

# Validate that ratings are numeric and between 0 and 10.

# Continue until the user decides to stop.

# Calculates:

# Total number of months evaluated

# Total rating

# Average rating

# Classifies performance:

# Average Rating	Performance Level
# 9 – 10	Outstanding
# 7 – 8.99	Excellent
# 5 – 6.99	Satisfactory
# Below 5	Needs Improvement


while True:
    eid_input=input("enter employee id:")
    if eid_input.isdigit():
        eid=eid_input
        break
    else:
        print("enter only digits")
ename=input("enter name:")
rating=0
totalmonths=0
while True:
    month_rating=float(input(f"enter this month{totalmonths+1} rating:"))
    if 0<=month_rating<=10:
        rating+=month_rating
        totalmonths+=1
    else:
        print("enter only numbersfrom 1 to 10")
        continue
    employee_input=input("want to enter another rating(continue/stop):")
    if employee_input.lower()!='continue':
        break   
averagerating=rating/totalmonths
performance=''
if 9<=averagerating<=10:
    performance='outstanding'
elif 7<=averagerating<9:
    performance='excellent'
elif 5<=averagerating<7:
    performance='satisfactory'
else:
    performance='Need improvement'

print("\n------------- Employee Performance Report -------------")
print(f"Employee ID        : {eid}")
print(f"Employee Name      : {ename}")
print(f"Months Evaluated   : {totalmonths}")
print(f"Total Rating       : {rating:.2f}")
print(f"Average Rating     : {averagerating:.2f}")
print(f"Performance Level  : {performance}")
    

    


