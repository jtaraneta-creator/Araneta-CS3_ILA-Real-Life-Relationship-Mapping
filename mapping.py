class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print("Students enrolled:")
        for student in self.students:
            print(student.name)


course = Course("CS101", "Introduction to Python")

student1 = Student("S001", "Alice")
student2 = Student("S002", "Bob")

course.add_student(student1)
course.add_student(student2)

course.display_students()