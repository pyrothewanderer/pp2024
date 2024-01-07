def num_students():
    num_students=int(input("Number of students in the class: "))
    for _ in range(num_students):
        student_id=input("Student ID: ")
        student_name=input("Student name: ")
        student_dob=input("Student Date of Birth: ")
        students.append((student_id, student_name, student_dob))
        marks[student_id]={}

def courses_info():
    num_courses=int(input("Number of courses: "))
    for _ in range(num_courses):
        course_id=input("Course ID: ")
        course_name=input("Course name: ")
        courses.append((course_id, course_name))

def add_marks():
    course_id=input("Course ID to input marks: ")
    for student in students:
        student_id=student[0]
        marks_value=float(input(f"Input marks for student {student_id} in course {course_id}: "))
        marks[student_id][course_id]=marks_value

def courses_list():
    print("Name:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def student_list():
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Dob: {student[2]}")

def student_marks():
    course_id=input("Please enter course ID to see student marks: ")
    print("Student marks: ")
    for student in students:
        student_id=student[0]
        marks_value=marks[student_id].get(course_id)
        if marks_value is not None:
            print(f"Student ID: {student_id}, Marks: {marks_value}")

students = []
courses = []
marks = {}

while 1 < 2:
    print("1. Add students")
    print("2. Add courses")
    print("3. Add marks")
    print("4. Courses list")
    print("5. Students list")
    print("6. Show student marks for a course")
    print("0. Exit")
    choice = input("Please enter your choice: ")

    if choice == "1":
        num_students()
    elif choice == "2":
        courses_info()
    elif choice == "3":
        add_marks()
    elif choice == "4":
        courses_list()
    elif choice == "5":
        student_list()
    elif choice == "6":
        student_marks()
    elif choice == "0":
        break 
    else:
        print("Invalid choice. Choose again.")