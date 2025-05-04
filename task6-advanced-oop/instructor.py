from person import Person

class Instructor(Person):
    """Represents an instructor assigned to teach courses."""
    
    def __init__(self, name: str, age: int, department: str):
        super().__init__(name, age)
        self.department = department

    def role(self) -> str:
        return "Instructor"