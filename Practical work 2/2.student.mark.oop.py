# DATA SECTION

students = []
students_name = []
courses = []
courses_name = []
mark_courses = []
mark_c_name = []
num_student: int
num_course: int


class Base_class:
    name: str
    id: str

    def __init__(self, input_name, input_id) -> None:
        self.name = input_name
        self.id = input_id


class Student(Base_class):
    name: str
    id: str
    dob: str

    def __init__(self, input_name, input_id, input_dob) -> None:
        super().__init__(input_name, input_id)
        self.dob = input_dob

    def show(self):
        print(f"""Student {self.name}:
            Id {self.id}
            Dob {self.dob}""")

    @classmethod
    def enter(cls):
        name = input("Enter the name of student: ")
        id = input("Enter the Id of student: ")
        dob = input("Enter the Dob of student: ")
        return Student(name, id, dob)


class Course(Base_class):
    name: str
    id: str

    def __init__(self, input_name, input_id) -> None:
        super().__init__(input_name, input_id)

    def show(self):
        print(f"Course {self.name}: Id {self.id}")

    @classmethod
    def enter(cls):
        name = input("Enter the name of course: ")
        id = input("Enter the Id of course: ")
        return Course(name, id)


class Mark:
    course: str
    mark: list

    def __init__(self, input_course, input_marks) -> None:
        self.course = input_course
        self.mark = input_marks

    def show(self, students_list):
        print(f"Course {self.course}")
        for i, x in enumerate(students_list):
            print(f"\t{x.name}: {self.mark[i]}")


# ________________________________________________________________________________________________
# FUNCTION SECTION

def get_num_student():
    # Enter number of students
    while True:
        try:
            num_student = int(
                input("Enter the number of students in the class: "))
            if (num_student < 1):
                print("Number of student must be at least 0.\n")
            else:
                return num_student
        except ValueError:
            print(
                f"The value \"{num_student}\" is not an integer, please try again.\n")


def get_num_course():
    # Enter number of course
    while True:
        try:
            num_course = int(
                input("Enter the number of courses in the class: "))
            if (num_course < 1):
                print("Number of course must be at least 0.\n")
            else:
                return num_course
        except ValueError:
            print(
                f"The value \"{num_course}\" is not an integer, please try again.\n")


def enter_students(num_student, students, students_name):
    # Enter each student
    for i in range(num_student):
        print(f"Student {i+1}")
        students.append(Student.enter())
        print()
        students_name.append(students[i].name)


def enter_course(num_course, courses, courses_name):
    # Enter each course
    for i in range(num_course):
        print(f"Course {i+1}")
        courses.append(Course.enter())
        courses_name.append(courses[i].name)
        print()


def enter_mark(mark_c_name, mark_courses):
    # Enter mark
    while True:
        mark_course = input("Enter the course to give mark: ")
        if (mark_course in courses_name) and (mark_courses not in mark_c_name):
            break
        print(
            f"{mark_course} is not an available course or is a course that already have mark")
    mark_list = []
    for x in students_name:
        # get grade
        while True:
            try:
                student_grade = float(input(f"Enter the mark for {x}: "))
                if (student_grade < 0):
                    print("The mark must be at least 0.\n")
                else:
                    mark_list.append(student_grade)
                    break
            except ValueError:
                print(f"{student_grade} is not a number.\n")
    mark_courses.append(Mark(mark_course, mark_list))
    mark_c_name.append(mark_course)


def list_student(students):
    if len(students) > 0:
        for item in students:
            item.show()
    else:
        print("There is no student data to list now. You must enter student data first\n")


def list_course(courses):
    if len(courses) > 0:
        for item in courses:
            item.show()
    else:
        print("There is no course data to list now. You must enter course data first\n")


def list_mark(mark_courses, mark_c_name):
    if (len(mark_courses) > 0):
        while True:
            c_name = input("Enter course to show mark: ")
            if c_name in mark_c_name:
                mark_courses[mark_c_name.index(c_name)].show(students)
                break
            else:
                print(f"{c_name} is not a course that has mark\n")
    else:
        print("There is not mark data to list now.\n")


# ________________________________________________________________________________________________
# MAIN SECTION

def main():
    while True:
        choice = input(
            "What do you want to do. Input data(I/i), List data(L/l) or exit(E/e): ").lower()
        if choice == "i":
            while True:
                choice = input(
                    "Do you want to input student(S/s), course(C/c) or mark(M/m) data: ").lower()
                if choice == "s":
                    num_student = get_num_student()
                    enter_students(num_student, students, students_name)
                    break
                elif choice == "c":
                    num_course = get_num_course()
                    enter_course(num_course, courses, courses_name)
                    break
                elif choice == "m":
                    if (len(students_name)*len(courses_name) != 0):
                        enter_mark(mark_c_name, mark_courses)
                    else:
                        print(
                            "There is no data for either student or course, can't enter mark now.\n")
                    break
                else:
                    print(
                        f"Option {choice} is not available, please try again.\n")
        elif choice == "l":
            while True:
                choice = input(
                    "Which do you want to list, student(S/s), course(C/c) or mark(M/m) data: ").lower()
                if choice == "s":
                    list_student(students)
                    break
                elif choice == "c":
                    list_course(courses)
                    break
                elif choice == "m":
                    list_mark(mark_courses, mark_c_name)
                    break
                else:
                    print(
                        f"Option {choice} is not available, please try again.\n")
                pass
        elif choice == "e":
            print("Thanks for using. Goodbye!\n")
            exit()
        else:
            print(f"Option {choice} is not available, please try again.\n")


if __name__ == "__main__":
    main()
