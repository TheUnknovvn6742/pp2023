import copy
num_student = None
num_course = None
students = []
courses = []
mark = {}
courses_name = []
students_name = []
student_prototype = {"Name":None, "Id": None, "DoB": None}
course_prototype = {"Name":None, "Id": None}
# Enter number of students
while True:
    num_student = int(input("Enter the number of students: "))
    if num_student > 0:
        print()
        break
    print("Students number must be bigger than 0.\n")

# Enter each student
for i in range(num_student):
    students.append(copy.deepcopy(student_prototype))
    name = input(f"Enter the {i+1} student name: ")
    id = input(f"Enter the {i+1} student id: ")
    dob = input(f"Enter the {i+1} student Dob: ")
    students[i]["Name"] = name
    students_name.append(name)
    students[i]["Id"] = id
    students[i]["DoB"] = dob
    print()

# Enter number of courses
while True:
    num_course = int(input("Enter the number of courses: "))
    if num_course > 0:
        print()
        break
    print("Courses number must be bigger than 0.\n")


# Enter each courses
for i in range(num_course):
    courses.append(copy.deepcopy(course_prototype))
    name = input(f"Enter the {i+1} course name: ")
    id = input(f"Enter the {i+1} course id: ")
    courses[i]["Name"] = name
    courses[i]["Id"] = id
    courses_name.append(name)

# Enter mark for a course
print()
while True:
    course = input("Enter the course to give mark: ")
    if course in courses_name:
        break
    print(f"{course} is not in the available courses.\n")


mark[course] = {}
for i in students_name:
    while True:
        x = float(input(f"Enter {course} mark for {i}: "))
        if x >= 0:
            break
        print("Students mark must not be negative.\n")
    mark[course][i] = x

# Listing courses
print(f"\nThere are {len(courses_name)} courses")
for i in courses:
    print(f'{i["Name"]} has id {i["Id"]}')

# Listing students
print(f"\nThere are {len(students_name)} students")
for i in students:
    print(f'{i["Name"]} has id {i["Id"]} and Dob {i["DoB"]}')

# Listing mark
while True:
    course = input("\nEnter the course to show mark: ")
    if course in courses_name:
        break
    print(f"{course} is not in the available courses.")

print(f"For course {course}:")
for i, j in mark[course].items():
    print(f'Students {i}: {j}')

