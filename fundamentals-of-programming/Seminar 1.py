# Calculate the area of different shapes without abstraction print("Calculate the area of a rectangle:")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
print(f"Area of the rectangle: {length * width}")

print("\nCalculate the area of a triangle:")
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
print(f"Area of the triangle: {0.5 * base * height}")

print("\nCalculate the area of a circle:")
radius = float(input("Enter the radius: "))
print(f"Area of the circle: {3.14159 * radius**2}")

#The code has duplication of logic because similar steps (input, calculation, and output)
#are repeated for each shape. It also lacks structure since it doesn’t use functions,
#making it harder to maintain and extend.

#Apply Procedural Abstraction
#Review this example which show the same code after it has been refactored by introducing functions:

def calculate_rectangle_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    return length * width

def calculate_triangle_area():
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    return 0.5 * base * height

def calculate_circle_area():
    radius = float(input("Enter the radius: "))
    return 3.14159 * radius**2
# Main Program
print("Calculate the area of a rectangle:")
print(f"Area of the rectangle: {calculate_rectangle_area()}")

print("\nCalculate the area of a triangle:")
print(f"Area of the triangle: {calculate_triangle_area()}")

print("\nCalculate the area of a circle:")
print(f"Area of the circle: {calculate_circle_area()}")

#The functions provide abstraction by hiding the input and calculation logic inside separate blocks.
# The main program simply calls these functions without needing to know how the calculations are performed.
# This makes the code easier to read, maintain, and reuse.

