#Financial Transaction Program
# Display the main menu options to the user
print("choose from the following options:")
print("1. Add income")
print("2. Add expense")
print("3. Exit")

# Get the user's main menu choice
main_choice = input("Enter your choice: ")

# Check if the user wants to add income
if main_choice == "1":
# Display income categories
    print("1.Salary")
    print("2.Freelance")
    print("3.Other")
# Get the user's choice of income type
income_choice = input("Enter your choice: ")
# If user selects Salary
if income_choice == "1":
 # Ask user to enter the income amount
       amount = input("Enter amount")
# Display confirmation
       print("Salary added" , amount)

# If user selects Freelance
elif income_choice == "2":
# Ask user to enter the income amount
        amount = input("Enter amount")
# Display confirmation
        print("Freelance added" , amount)

# If user selects Other
elif income_choice  == "3":
# Ask user to enter the income amount
        amount = input("Enter amount")
# Display confirmation
        print("Other" , amount)






