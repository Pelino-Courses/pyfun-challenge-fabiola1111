import math

class Shape:
    """
    Base class for all geometric shapes.

    Available shape options:
    1. Circle
    2. Rectangle
    3. Triangle
    4. Exit

    
    """
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        return f"{self.name} Shape"

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"{self.name} with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"{self.name} with width {self.width} and height {self.height}"

class Triangle(Shape):
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"{self.name} with base {self.base} and height {self.height}"


def main():
    print("Welcome to the Geometric Shape Calculator!")
    while True:
        print("\n" + "-" * 40)
        print(Shape.__doc__)
        print("-" * 40)
        choice = input("Choose a shape (1–4): ")

        try:
            if choice == "1":
                radius = float(input("Enter radius of the circle: "))
                shape = Circle(radius)

            elif choice == "2":
                width = float(input("Enter width of the rectangle: "))
                height = float(input("Enter height of the rectangle: "))
                shape = Rectangle(width, height)

            elif choice == "3":
                base = float(input("Enter base of the triangle: "))
                height = float(input("Enter height of the triangle: "))
                shape = Triangle(base, height)

            elif choice == "4":
                print("Thank you for using the shape calculator!")
                break

            else:
                print("Invalid choice. Please select from 1–4.")
                continue

            print(f"\nYou created: {shape}")
            print(f"Area: {shape.area():.2f}")

        except ValueError as ve:
            print("Error:", ve)

if __name__ == "__main__":
    main()
