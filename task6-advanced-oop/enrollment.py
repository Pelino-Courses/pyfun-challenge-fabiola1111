from student import Student
from course import Course

class Enrollment:
    """Manages enrollment relationship between a student and a course."""
    
    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course
        student.enroll(course)

    def __str__(self):
        return f"{self.student.name} is enrolled in {self.course.title}"