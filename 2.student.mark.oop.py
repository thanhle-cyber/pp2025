class Entity:
    def input(self):
        pass
    def print(self):
        pass

class Student(Entity):
    def __init__(self):
        self.name=""
        self.id=""
        self.dob=""
    def input(self):
        self.name=input("Enter a student name:")
        self.id=input("Enter student id:")
        self.dob=input("Enter student dob")
    def print(self):
        print(f"Student name: {self.name} | Student id:{self.id} | Student DOB:{self.dob}")
class Course(Entity):
    def __init__(self):
        self.cname=""
        self.cid=""
    def input(self):
        self.cname=input("Enter course name:")
        self.cid=input("Enter course id:")
    def print(self):
        print(f"Course name:{self.cname} | Course id:{self.cid}")
class Mark(Entity):
    def __init__(self,student,course,mark):
        self.mark=mark
        self.student=student
        self.course=course
    def input(self):
        self.mark=float(input(f"Enter mark for student {self.student.name}:"))
    def print(self):
        print(f"Mark for student{self.student.name} for course {self.course.cname} is {self.mark}")
class School():
    def __init__(self):
        self.students=[]
        self.courses=[]
        self.marks=[]
    def input_student(self):
        n= int(input("Enter number of student:"))
        for i in range(1,n+1):
            s=Student()
            s.input()
            self.students.append(s)
    def input_courses(self):
        n=int(input("Enter number of courses:"))
        for i in range(n):
            c=Course()
            c.input()
            self.courses.append(c)
    def list_course(self):
        for i in self.courses:
            i.print()
    def list_student(self):
        for i in self.students:
            i.print()
    def find_course(self,cid):
        for i in self.courses:
            if i.cid ==cid :
                return i
            else: return None

    def find_student(self,id):
        for s in self.students:
            if s.id==id:
                return s
            else: return None
                
    
    def input_mark(self):
        print("Available course:")
        self.list_course()
        cid=input("Enter course id:")
        course=self.find_course(cid)
        for i in self.students:
            m=float(input(f"Enter mark for student {i.name} for course {course.cname}:"))
            mark_obj=Mark(i,course,m)
            self.marks.append(mark_obj)
    def show_mark_for_course(self):
        cid=input("Enter course id:")
        course=self.find_course(cid)
        print(f"Mark for course {course.cname} \n")
        for m in self.marks:
            if m.course.cid == cid:
                m.print()
school=School()
school.input_student()
school.input_courses()
school.input_mark()
school.show_mark_for_course()




