from student import Student
from instructor import Instructor
from course import Course
class Enrollment:
    def __init__(self):
        self.enrollments: list['int'] =  []

    def enroll_student(self, student_name: str, course_name: str, instructor_name) -> str:
        student = Student(student_name, course_name)
        course = Course(student.course)
        course.display_course_info()
        instructor = Instructor(course.instructor, student.course)
        instructor.course = course_name
        self.instructor_name = instructor_name
        enrollment_record : dict["str", "str"] = {
            "student_name": student.name,
            "course_name": student.course,
            "instructor_name": instructor.name
        }
        self.enrollments.append(enrollment_record)
        return f"Enrolled {student.name} in {student.course} under {self.instructor_name}"

    def display_enrollments(self) -> str:
        if not self.enrollments:
            return "No enrollments available"
        return "\n".join(
            f"Student: {record['student_name']}, Course: {record['course_name']}, Instructor: {record['instructor_name']}" for record in self.enrollments
        )

