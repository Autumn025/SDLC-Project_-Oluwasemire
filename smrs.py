# Student Result Management System (SRMS)
# Preloaded Data for SEN Assignment
# Student ID: 24/13790
# Student Name: LAOYE OLUWASEMIRE OLUWATIMILEHIN
# Course: SEN 201
# Result: A

# =======================
# DATA STORAGE
# =======================

students = {
    "24/13790": "LAOYE OLUWASEMIRE OLUWATIMILEHIN"
}

courses = {
    "SEN 201": "Software Engineering"
}

results = {
    "24/13790": {
        "SEN 201": ("A",)
    }
}

# =======================
# FUNCTION DEFINITIONS
# =======================

def add_student():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    if student_id in students:
        print("Student already exists.\n")
    else:
        students[student_id] = student_name
        print("Student added successfully.\n")

def add_course():
    course_code = input("Enter Course Code: ")
    course_title = input("Enter Course Title: ")

    if course_code in courses:
        print("Course already exists.\n")
    else:
        courses[course_code] = course_title
        print("Course added successfully.\n")

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"

def add_result():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")

    if student_id not in students:
        print("Student not found.\n")
        return

    if course_code not in courses:
        print("Course not found.\n")
        return

    try:
        score = int(input("Enter Score: "))
    except ValueError:
        print("Invalid score.\n")
        return

    grade = calculate_grade(score)

    if student_id not in results:
        results[student_id] = {}

    results[student_id][course_code] = (grade,)
    print("Result recorded successfully.\n")

def view_results():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.\n")
        return

    print(f"\nResults for {students[student_id]}:")

    if student_id in results:
        for course_code, grade_data in results[student_id].items():
            grade = grade_data[0]
            course_title = courses.get(course_code, "Unknown Course")
            print(f"{course_code} - {course_title}: Grade = {grade}")
    else:
        print("No results available.")

    print()

# =======================
# MAIN APPLICATION
# =======================

def main():
    while True:
        print("===== STUDENT RESULT MANAGEMENT SYSTEM (SRMS) =====")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Add Result")
        print("4. View Results")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            add_result()
        elif choice == "4":
            view_results()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()