from person import Person
class Student(Person):
    def __init__(self, name: str, course=None):
        super().__init__(name)
        self.course = course
        self.grades = None

    students_list = {}
    def register_students(self) -> list:
        # student_names = input("Enter names sepataed by comma: ")
        # self.students = student_names.split(',') 
        self.grade = input("Grades you have: ")
        # register student
        student_id = len(Student.students_list) + 1
        student: dict['str', 'str'] =  {
            "name": self.name,
            "grade": self.grade
        }   
        Student.students_list[student_id] = student
        return Student.students_list
    def display_student_info(self) -> str:
        return f"Student name: {self.name}, courses: {self.course}"
