# Requirements

# Accept Patient ID

# Must contain digits only (isdigit() check)

# Accept Patient Name

# Enter multiple test results using a loop

# Each test has a name and a score (0–100)

# Validate numeric score input

# Continue until user types “no”

# Compute:

# Total number of tests

# Total and average score

# Classify Health Condition based on the average score:

# Average Score	Health Status
# 90–100	Excellent Health
# 70–89	Good Health
# 50–69	Moderate Health
# Below 50	Poor Health – Needs Checkup

# Ask for BMI (Body Mass Index)

# BMI < 18.5 → Underweight

# 18.5–24.9 → Normal

# 25–29.9 → Overweight

# ≥ 30 → Obese

# 🏥 Patient Health Report System


while True:
    pid_input = input("Enter Patient ID: ")
    if pid_input.isdigit():
        pid = pid_input
        break
    else:
        print("Invalid ID! Enter digits only.")

pname = input("Enter Patient Name: ").title()

tests = []
total_score = 0
num_tests = 0

while True:
    test_name = input(f"Enter Test {num_tests + 1} Name: ").title()
    try:
        test_score = float(input(f"Enter {test_name} Score (0-100): "))
        if 0 <= test_score <= 100:
            tests.append({"name": test_name, "score": test_score})
            total_score += test_score
            num_tests += 1
        else:
            print("Score must be between 0 and 100.")
            continue
    except ValueError:
        print("Invalid input! Enter a numeric value.")
        continue

    more = input("Do you want to enter another test? (yes/no): ").lower()
    if more != 'yes':
        break

if num_tests > 0:
    avg_score = total_score / num_tests
else:
    avg_score = 0

if 90 <= avg_score <= 100:
    health_status = "Excellent Health"
elif 70 <= avg_score < 90:
    health_status = "Good Health"
elif 50 <= avg_score < 70:
    health_status = "Moderate Health"
else:
    health_status = "Poor Health Needs Checkup"

bmi=float(input("enter bmi:"))

if bmi < 18.5:
    bmi_category = "Underweight"
elif 18.5 <= bmi < 25:
    bmi_category = "Normal"
elif 25 <= bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

print("\n---------------- Patient Health Report ----------------")
print(f"Patient ID         : {pid}")
print(f"Patient Name       : {pname}")
print("--------------------------------------------------------")
print("Tests Performed:")
for test in tests:
    print(f"{test['name']:<20} : {test['score']}")
print("--------------------------------------------------------")
print(f"Total Tests        : {num_tests}")
print(f"Average Score      : {avg_score:.2f}")
print(f"Health Condition   : {health_status}")
print(f"BMI Value          : {bmi:.2f}")
print(f"BMI Category       : {bmi_category}")

if avg_score < 50:
    print(" ALERT: Patient requires medical attention due to low test performance.")
if bmi >= 30:
    print("ALERT: Patient is obese. Recommend lifestyle changes or consultation.")

     
     