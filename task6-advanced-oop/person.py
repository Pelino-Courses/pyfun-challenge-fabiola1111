from abc import ABC, abstractmethod

class Person(ABC):
    """Abstract base class for a person in the university."""
    
    def __init__(self, name: str, age: int):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        self.name = name
        self.age = age

    @abstractmethod
    def role(self) -> str:
        pass

    def __str__(self):
        return f"{self.role()}: {self.name}, Age: {self.age}"