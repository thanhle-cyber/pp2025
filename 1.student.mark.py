students = []  
def add_student():
    students.append({"id": input("ID: "), "name": input("Name: "), "marks": []})

def add_mark():
    sid = input("Student ID: ")
    for s in students:
        if s["id"] == sid:
            s["marks"].append((input("Subject: "), int(input("Mark: "))))
            break

def view_students():
    for s in students:
        print(f"{s['id']} - {s['name']} | {s['marks']}")

def avg_mark():
    sid = input("Student ID: ")
    for s in students:
        if s["id"] == sid and s["marks"]:
            print(sum(m for _, m in s["marks"]) / len(s["marks"]))
            break

while True:
    c = input("\n1.Add Student 2.Add Mark 3.View 4.Avg 5.Exit\nChoice: ")
    if c=="1": add_student()
    elif c=="2": add_mark()
    elif c=="3": view_students()
    elif c=="4": avg_mark()
    elif c=="5": break
print("Hello")