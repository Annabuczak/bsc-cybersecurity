try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Sorry, that's not a valid age.")

try:
    number = 123 / 0
except ZeroDivisionError:
    print("Sorry, that's not a valid number.")
file = open("file.txt", "w")
try:
    print(file.read())
finally:
    file.close()

age = -22

if age < 0:
    print("Sorry, that's not a valid age.")
raise ValueError
