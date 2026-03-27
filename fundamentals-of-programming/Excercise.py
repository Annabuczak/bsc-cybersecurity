#Exercise: Applying Abstraction
#Review the code below class Shape

class Shape:
 def __init__(self, name):
    self.name = name
    def calculate_area(self):

    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius**2 # Example Usage
shapes = [ Rectangle(5, 10), Triangle(8, 12), Circle(7) ]

for shape in shapes:
    print(f"The area of the {shape.name} is: {shape.calculate_area()}")