student=[]
courses=[]
marks={}
def input_number_of_student():
    return int(input("Enter number of student"))
def input_student_information():
    student_id=input("Student ID")
    name=input("student name")
    dob=input("Student date of birth")
    return{"id":student_id,"name":name,"DOB":dob}
def input_number_of_courses():
    return int(input("Enter number of courses:"))
def input_courses_information():
    course_id=input("Enter course id:")
    course_name=input("Enter course name:")
    return{"courseid":course_id,"coursename":course_name}
def list_courses():
    for c in courses:
        print(f"course ID:{c['courseid']} | Name:{c['coursename']}")
    print()
def list_student():
    for s in student:
        print(f"Student id:{s['id']} | Name: {s['name']} | DOB: {s['DOB']}")
    print()
def input_mark_for_course():
    list_courses()
    course_id=input("Enter course id:")
    for st in student:
        mark=float(input(f"enter mark for student {st['name']} | ID: {st['id']}"))
        marks[course_id][st['id']]=mark
def show_marks_for_course():
    list_courses()

    course_id = input("Enter course ID to view marks: ")

    print(f"\n--- MARKS FOR COURSE {course_id} ---")
    for st in student:
        sid = st["id"]
        if sid in marks[course_id]:
            print(f"{st['name']} ({sid}): {marks[course_id][sid]}")
        else:
            print(f"{st['name']} ({sid}): No mark yet")
    print()
n_students = input_number_of_student()
for _ in range(n_students):
    student.append(input_student_information())

# Input courses
n_courses = input_number_of_courses()
for _ in range(n_courses):
    courses.append(input_courses_information())

# Menu loop
while True:
    print("\n1. Enter marks")
    print("2. List students")
    print("3. List courses")
    print("4. Show marks for a course")
    print("0. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        input_mark_for_course()
    elif choice == "2":
        list_student()
    elif choice == "3":
        list_courses()
    elif choice == "4":
        show_marks_for_course()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")