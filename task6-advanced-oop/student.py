from person import Person
from typing import List, Iterator

class Student(Person):
    """Represents a student who can enroll in courses."""
    
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self._courses: List['Course'] = []

    def enroll(self, course: 'Course'):
        if course not in self._courses:
            self._courses.append(course)
            course.add_student(self)

    def __iter__(self) -> Iterator['Course']:
        return iter(self._courses)

    def __add__(self, other: 'Student') -> List['Course']:
        return list(set(self._courses + other._courses))

    def role(self) -> str:
        return "Student"