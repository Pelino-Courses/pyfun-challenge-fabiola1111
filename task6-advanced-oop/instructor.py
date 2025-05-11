from person import Person
from student import Student

class Instructor(Person):
    def __init__(self, name, course=None):
        self.course = course
        super().__init__(name)
        
    def view_student(self):
        # students = [st for st in self.student_list]
        students_info = []
        for student_id, student_data in Student.students_list.items():
            students_info.append(
                f"ID: {student_id}, Name: {student_data['name']}, Courses: {', '.join(student_data['courses'])}"
            )
        return "\n".join(students_info)
    def display_instructor_info(self):
        return f"The name of instractor is: {self.name} and Teaches {self.course}"