class Student:
    def __init__(self, name, age, grade, student_id):
        self.name = name
        self.age = age
        self.grade = grade
        self.__student_id = student_id  # This is a private attribute

    def __show_student_id(self):
        print(
            f"Private ID info{self.__student_id}"
        )

    def display_student_id(self):
        self.__show_student_id()

    def about_student(self):
        print(f"This cyber security student {self.name} is {self.age} years old and has a grade of {self.grade}.")


student = Student("Alan", 18, 90, 1212)

student_id = 1212
student.about_student()
student.display_student_id()
