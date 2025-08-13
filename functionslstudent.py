SYSTEM_INFO = ("LMS Students Portal","v1.0","Edify University")
ADMIN_INFO = ("admin@edify.ai","+91-9876543210","201")

students = {}

def add_student():
    print("Performing Add Student Operation")
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student Already Exists")
        return

    name = input("Enter Student Name: ").strip().title()
    scores = []
    while True:
        score_input = input("Enter a score or type 'done': ")
        if score_input.lower() == "done":
            break
        if score_input.isdigit():
            score = int(score_input)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Invalid Score, only 0-100")
        else:
            print("Invalid input. Only numbers accepted.")

    skills = set()
    while True:
        skill_input = input("Enter a skill or type 'done': ")
        if skill_input.lower() == "done":
            break
        skills.add(skill_input.strip().title())

    students[student_id] = {
        "name": name,
        "scores": scores,
        "skills": skills
    }

    print("Student Added Successfully.")

def modify_student():
    print("Performing Modify Student Operation")
    student_id = input("Enter Student ID to Modify: ")
    if student_id in students:
        new_name = input("Enter New Name: ").strip().title()
        students[student_id]["name"] = new_name
        print("Student Updated Successfully")
    else:
        print("Student ID Not Found")

def delete_student():
    print("Performing Delete Student Operation")
    student_id = input("Enter Student ID to Delete: ")
    removed = students.pop(student_id, None)
    if removed:
        print("Student Deleted Successfully")
    else:
        print("Student ID Not Found")

def list_all_students():
    print("Performing Choice 4 Operation")
    if not students:
        print("No Students Available")
    else:
        print("All Students Information")
        for sid, data  in students.items():
            name = data["name"] 
            scores = data["scores"] 
             
            if scores:
                avg = sum(scores) / len(scores)
            else:
                avg = 0    
            if scores:
                top_score = max(scores)
            else:
                top_score = 0
        
            skills =  data["skills"]

        print(f"ID: {sid}")
        print(f"Name: {name}")
        print(f"Scores: {scores}")
        print(f"Average Score: {avg}")
        print(f"Top Score: {top_score}")
        print(f"Skills: {skills}")
        print(f"Skills Count: {len(skills)}")
        print("-" * 30)

def search_by_skill():
    print("Performing Search By Skill Operation")
    skill_to_search = input("Enter skill to search: ").strip().title()
    matched_students = list(filter(lambda item: skill_to_search in item[1]["skills"], students.items()))
    if matched_students:
        for sid, data in matched_students:
            print(f"ID: {sid}")
            print(f"Name: {data['name']}")
            print(f"Scores: {data['scores']}")
            print(f"Skills: {data['skills']}")
            print("-" * 30)
    else:
        print(f"No students found with skill: {skill_to_search}")

def exit_app():
    print("Performing Exit Operation")
    print("=" * 50)
    print("Contact Admin For Further Help")
    print(f"Mobile Number: {ADMIN_INFO[1]}")
    print(f"Email ID: {ADMIN_INFO[0]}")
    print("=" * 50)

def main():
    print("="*50)
    print(f"Welcome To {SYSTEM_INFO[0]} {SYSTEM_INFO[1]}")
    print(f"Developed By {SYSTEM_INFO[2]} students ")
    print("="*50)
    while True:
        print("Choose an option:")
        print("1 - Add Student")
        print("2 - Modify Student")
        print("3 - Delete Student")
        print("4 - List All Students")
        print("5 - Search Skill")
        print("6 - Exit App")

        choice = input("Enter Your Choice (1-6): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            modify_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            list_all_students()
        elif choice == "5":
            search_by_skill()
        elif choice == "6":
            exit_app()
            break
        else:
            print("Invalid Choice. Please select only (1-6)")
main()