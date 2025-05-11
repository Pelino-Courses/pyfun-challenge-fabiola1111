from person import Person
from student import Student
from instructor import Instructor

class Course:
    """
    Course class to manage course information, students and instructors.
    """
    def __init__(self, name: str):
        """
        Initialize a new course
        Args:
            name (str): Name of the course
        """
        self.name = name
        self.instructor = None
        self.students = []

    def set_instructor(self, instructor: Instructor):
        """
        Assign an instructor to the course
        Args:
            instructor (Instructor): Instructor object to assign
        """
        self.instructor = instructor

    def add_student(self, student: Student):
        """
        Add a student to the course
        Args:
            student (Student): Student object to add
        """
        if student not in self.students:
            self.students.append(student)

    def display_course_info(self):
        """
        Display course information including instructor and enrolled students
        Returns:
            str: Formatted course information
        """
        info = f"Course: {self.name}\n"
        if self.instructor:
            info += f"Instructor: {self.instructor.name}\n"
        
        if self.students:
            info += "Enrolled Students:\n"
            for student in self.students:
                info += f"- {student.name}\n"
        return info

    def __str__(self):
        return f"Course: {self.name}"


