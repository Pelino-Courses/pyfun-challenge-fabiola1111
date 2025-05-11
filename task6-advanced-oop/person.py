class Person:
    def __init__(self, name):
        self.name = name

    def student(self, course, grade, name, courses: list, enrolled: list):
        self.name = name
        self.courses = courses
        self.enrolled = enrolled
        self.grade = grade
        return f"{self.name} is enrolled in {self.courses} with a grade of {grade}."
    
    def instructor(self, name, course):
        self.teacher_name = name
        self.students = []
        self.course = course

        return f"Teacher name is {self.teacher_name} and he teaches {self.students}"
