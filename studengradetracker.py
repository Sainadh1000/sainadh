while True:
    student_id_input = input("Enter Student ID: ")
    if student_id_input.isdigit():
        student_id = student_id_input
        break
    else:
        print("invalid student id")
student_name = input("Enter Student Name: ")
while True:
    try:
        attendance = float(input("Enter Attendance Percentage (%): "))
        if 0 <= attendance <= 100:
            break
        else:
            print("Attendance must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for attendance.")
total_score = 0
num_subjects = 0
while True:
    try:
        score = float(input(f"Enter score for subject {num_subjects + 1}: "))
        if 0 <= score <= 100:
            total_score += score
            num_subjects += 1
        else:
            print("Score must be between 0 and 100.")
            continue
    except ValueError:
        print("Invalid input. Please enter a numeric score.")
        continue

    cont = input("Do you want to enter another score? (Yes/No): ")
    if cont.lower() != 'yes':
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
    attendance_status = "WARNING: Low Attendance" 
else:
    attendance_status= "OK: Attendance Satisfied"

print("\n------------------- Student Details -------------------")
print(f"Student ID        : {student_id}")
print(f"Student Name      : {student_name}")
print(f"Total Subjects    : {num_subjects}")
print(f"Total Score       : {total_score}")
print(f"Average Score     : {average_score:.2f}")
print(f"Performance Level : {performance}")
print(f"Attendance (%)    : {attendance:.2f}%")
print(f"Attendance Status : {attendance_status}")