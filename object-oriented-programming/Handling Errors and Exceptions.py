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
