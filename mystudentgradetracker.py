student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
attendance = float(input("Enter Attendance Percentage (%): "))
total_score = 0
num_subjects = 0
while True:
    try:
        score =float(input(f"Enter score for subject {num_subjects + 1}: "))
        total_score += score
        num_subjects += 1
    except ValueError:
        print("Invalid input. Please enter a numeric score.")
        continue

    cont = input("Do you want to enter another score? (Yes/No): ")
    if cont != 'yes':
        break 
if num_subjects > 0:
    average_score = total_score / num_subjects
else:
    average_score = 0
if average_score >= 85:
    performance = "Excellent"
elif 70 <= average_score < 85:
    performance = "Good"
elif 50 <= average_score < 70:
    performance = "Average"
else:
    performance = "Needs Improvement"
if attendance < 75:
    attendance_status = " WARNING: Low Attendance"
else:
    attendance_status = "OK: Attendance Satisfied"
print("-------------------display details--------------------")
print(f"Student ID        : {student_id}")
print(f"Student Name      : {student_name}")
print(f"Total Subjects    : {num_subjects}")
print(f"Total Score       : {total_score}")
print(f"Average Score     : {average_score:}")
print(f"Performance Level : {performance}")
print(f"Attendance (%)    : {attendance}%")
print(f"Attendance Status : {attendance_status}")
