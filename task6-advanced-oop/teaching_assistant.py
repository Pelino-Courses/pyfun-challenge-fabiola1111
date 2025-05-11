from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    """
    Teaching Assistant class that inherits from both Student and Instructor.
    
    Attributes:
        name (str): Name of the teaching assistant
        course (str): Course they are assisting with
        grades (float): Their academic performance grade
        assisting_instructor (str): Name of instructor they're assisting
    """
    
    def __init__(self, name: str, course: str = None, grades: float = None):
        """
        Initialize a teaching assistant with both student and instructor capabilities
        
        Args:
            name (str): Name of the teaching assistant
            course (str, optional): Course they are assisting with
            grades (float, optional): Their academic grades
        """
        # Call both parent class constructors
        Student.__init__(self, name, course)
        Instructor.__init__(self, name, course=None)
        self.grades = grades
        self.course = course
        self.assisting_instructor = None

    def instructor_to_assist(self, instructor_name: str, course: str) -> str:
        """
        Assign the TA to assist an instructor
        
        Args:
            instructor_name (str): Name of instructor to assist
            course (str): Course to assist with
        
        Returns:
            str: Confirmation message
        """
        self.course = course
        self.assisting_instructor = instructor_name
        return f"Teaching assistant {self.name} is assisting instructor {instructor_name}"

    def student_to_teach(self, course: str, grade: float) -> str:
        """
        Record student teaching activity and grade
        
        Args:
            course (str): Course being taught
            grade (float): Teaching performance grade
        
        Returns:
            str: Status message
        """
        self.course = course
        self.grades = grade
        return f"Teaching assistant: {self.name} is teaching the course {course} with grade {grade}"

    def display_info(self) -> str:
        """
        Display teaching assistant information
        
        Returns:
            str: Formatted information string
        """
        info = f"Teaching assistant name: {self.name}\n"
        info += f"Course: {self.course}\n"
        if self.grades:
            info += f"Grade: {self.grades}\n"
        if self.assisting_instructor:
            info += f"Assisting: {self.assisting_instructor}"
        return info