class Person:
    def __init__(self,id,name):
        self._id=id
        self._name=name
        def get_id(self):
            return self._id
        def get_name(self):
            return self._name
class Student(Person):
    def __init__(self, id, name,dob):
        super().__init__(id,name)
        self._dob=dob
    def get_dob(self):
        return self._dob
    def List_info(self):
        print(f"ID: {self._id} | Name:{self._name} | DOB: {self._dob}")
class Course:
    def __init__(self,cid,cname):
        self._id=cid
        self._name=cname
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
class MarkManager:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}   
    def input_students(self):
        n = int(input("Enter number of students: "))
        for _ in range(n):
            sid = input("Student ID: ")
            name = input("Student name: ")
            dob = input("Student DOB: ")
            s = Student(sid, name, dob)
            self._students.append(s)

    def list_students(self):
        print("\n--- STUDENT LIST ---")
        for s in self._students:
            s.list_info()
        print()

    def input_courses(self):
        n = int(input("Enter number of courses: "))
        for _ in range(n):
            cid = input("Course ID: ")
            name = input("Course name: ")
            c = Course(cid, name)
            self._courses.append(c)

    def list_courses(self):
        print("\n--- COURSE LIST ---")
        for c in self._courses:
            c.list_info()
        print()

    def input_marks(self):
        self.list_courses()
        cid = input("Enter course id to input marks: ")

        if cid not in self._marks:
            self._marks[cid] = {}

        print(f"\nEntering marks for course {cid}:")
        for s in self._students:
            mark = float(input(f"Enter mark for {s.get_name()} ({s.get_id()}): "))
            self._marks[cid][s.get_id()] = mark

        print("Marks updated!\n")

    def show_marks(self):
        self.list_courses()
        cid = input("Enter course ID to show marks: ")

        print(f"\n--- MARKS FOR COURSE {cid} ---")
        course_marks = self._marks.get(cid, {})

        for s in self._students:
            sid = s.get_id()
            if sid in course_marks:
                print(f"{s.get_name()} ({sid}): {course_marks[sid]}")
            else:
                print(f"{s.get_name()} ({sid}): No mark")
        print()



def main():
    manager = MarkManager()
    manager.input_students()
    manager.input_courses()
    while True:
        print("\n1. Enter marks")
        print("2. List students")
        print("3. List courses")
        print("4. Show marks for a course")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            manager.input_marks()
        elif choice == "2":
            manager.list_students()
        elif choice == "3":
            manager.list_courses()
        elif choice == "4":
            manager.show_marks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

    
