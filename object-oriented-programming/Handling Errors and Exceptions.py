# Restaurant Bill Splitter

try:
    total_bill = float(input("Enter total bill: £"))
    num_people = int(input("Enter number of people: "))

    bill_per_person = total_bill / num_people

    print(f"Each person should pay: £{bill_per_person:.2f}")

except ValueError:
    print("Invalid input. Please enter numbers only.")

except ZeroDivisionError:
    print("Number of people cannot be 0.")


# Student Marks File Reader
def read_marks(filename):
    try:
        with open(filename, "r") as file:
            marks = []

            for line in file:
                mark = int(line.strip())  # May raise ValueError
                marks.append(mark)

            return marks

    except FileNotFoundError:
        raise


try:
    marks = read_marks("marks.txt")
    print("Marks:", marks)

except FileNotFoundError:
    print("marks.txt not found.")

except ValueError:
    print("One of the marks in the file is invalid.")
