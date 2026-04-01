#Financial Transaction Program
# Display the main menu options to the user
transactions = []
def show_menu():
 print("\n--Financial Transaction Program--")
 print("1. Add income")
 print("2. Add expense")
 print("3. View transactions")
 print("4. View balance")
while True:
    show_menu()
    choice = input("Enter your choice: ").strip()
    if choice == "1":
     print("1.Salary")
     print("2.Freelance")
     print("3.Other")
    income_choice = input("Enter your choice: ")

    if income_choice == "1":
       amount = input("Enter amount")
       print("Salary added" , amount)

    elif income_choice == "2":
        amount = input("Enter amount")
        print("Freelance added" , amount)

    elif income_choice  == "3":
         amount = input("Enter amount")
         print("Other" , "amount")

    elif income_choice == "4":
        print("Exiting...")

    else:
        print("Invalid input. Please choose 1-4.")

