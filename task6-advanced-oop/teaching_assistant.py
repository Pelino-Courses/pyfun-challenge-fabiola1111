from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    """A TA has student and instructor roles."""
    
    def __init__(self, name: str, age: int, department: str):
        # Student.__init__(self, name, age)
        Instructor.__init__(self, name, age, department)

    def role(self) -> str:
        return "Teaching Assistant"
obj = TeachingAssistant("d", 12, "rt")
print(obj.role())    