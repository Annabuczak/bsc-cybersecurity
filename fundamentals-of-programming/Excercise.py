# Exercise: Applying Abstraction
# Review the code below class Shape

# I reviewd the code below. I found several mistake in the code which I've fixed.
#1.calculate.area is now properly inside Shape, all subclasses override it, there are no random functions
#floating around, indentation is consistent. Program runs and produces correct output.
# Fixed code understand abstract idea of a shape, each class defines its own area formula,
# the loop treats them all the sane
class Shape:
      def __init__(self, name):
         self.name = name

      def calculate_area(self):
          pass

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius**2 # Example Usage
shapes = [Rectangle(length=5, width=10), Triangle(base=8, height=12), Circle(radius=7)]

for shape in shapes:
    print(f"The area of the {shape.name} is: {shape.calculate_area()}")

