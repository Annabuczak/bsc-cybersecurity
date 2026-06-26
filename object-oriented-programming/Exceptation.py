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
rint("Start")
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That is not a valid number")
print("End")

try:
    number = int("6.4")
    print("number created")
except:
    print("That is not a valid number")
print("End")
try:
    number = int("100")
    print(number * 2)
except ValueError:
    print("Error!")
print("Done")

try:
    print("One")
    print(10 / 2)
    print("Two")
    print(10 / 0)
    print("Three")

except ZeroDivisionError:
    print("Oops!")
print("End")
try:
    number = int("hello")
    print("A")
except ZeroDivisionError:
    print("B")
except ValueError:
    print("C")

print("D")

try:
    print("Start")
    x = int("5")
    print("Middle")
    y = 10 / 0
    print("End")
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Division Error")

print("Finished")


class UnderAgeError(Exception):
    pass


age = int(input("Enter your age: "))
try:
    if age < 18:
        raise UnderAgeError()
except ValueError:
    print("Enter valid number")
except UnderAgeError:
    print('Too young to enter')
else:
    print("Have a great time")
