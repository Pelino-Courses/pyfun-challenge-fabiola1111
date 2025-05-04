from person import Person
from course import Course
from typing import List, Iterator
course = Course("name", "nice")
class Student(Person):
    """Represents a student who can enroll in courses."""
    
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.courses = []

    def enroll(self, course):
        self.course=course
        if self.course not in self.courses:
            self.courses.append(self.course)
            course.add_student(self)

    def __iter__(self) -> list:
        return iter(self.courses)

    def __add__(self, other):
        return list(set(self.courses + other.courses))

    def role(self):
        return "Student"