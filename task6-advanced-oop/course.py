from typing import List, Iterator
from student import Student

class PositiveNumber:
    """Descriptor to ensure values are positive numbers."""
    def __init__(self, name):
        self.name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name[1:]} must be a positive number.")
        setattr(obj, self.name, value)

class Course:
    """Represents a course in the university."""
    
    credits = PositiveNumber("credits")

    def __init__(self, title: str, credits: int):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        self.title = title
        self.credits = credits
        self._students: List[Student] = []

    def add_student(self, student: Student):
        if student not in self._students:
            self._students.append(student)
            return "Student added"

    def __iter__(self) -> Iterator[Student]:
        return iter(self._students)

    def __str__(self):
        return f"{self.title} ({self.credits} credits)"

    @classmethod
    def create_lab_course(cls, title: str) -> 'Course':
        return cls(title, 1)

    @classmethod
    def create_lecture_course(cls, title: str) -> 'Course':
        return cls(title, 3)