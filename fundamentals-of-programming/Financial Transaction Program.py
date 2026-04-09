#Income
transactions = []

def show_menu():
    print("\n--Financial Transaction Program--")
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View balance")
    print("5. Go to main menu")

def add_transaction(t_type, t_amount, t_date, t_category):
    transactions.append({
        "type": t_type,
        "amount": t_amount,
        "date": t_date,
        "category": t_category
    })
    print(f"Success: ${t_amount} added to {t_category} on {t_date}.")
def show_balance(t_type, t_amount, t_date, t_category):
    transactions.append({
        "type": t_type,
        "amount": t_amount,
        "date": t_date,
        "category": t_category
    })
    print(f"Success: ${t_amount} added to {t_category} on {t_date}.")
while True:
    show_menu()

    choice = input("Enter your choice: ")
#income
    if choice == "1":
        print("1. Salary")
        print("2. Freelance")
        print("3. Other")

        income_choice = input("Enter your choice: ")

        if income_choice == "1":
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction("income", amount, date, "Salary")

        elif income_choice == "2":
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction("income", amount, date, "Freelance")

        elif income_choice == "3":
             amount = float(input("Enter amount: "))
             date = input("Enter date (YYYY-MM-DD): ")
             add_transaction("income", amount, date, "Other")

        else:
           print("Invalid income option.")
    elif choice == "3":

           if not transactions:
               print("No transactions yet.")
           else:
               for item in transactions:
                   print(f"Date: {item['date']} | {item['category']} ({item['type']}) | ${item['amount']}")
#expenses
    elif choice == "2":
     print("1. Set bills")
     print("2. Groceries")
     print("3. Transport")
     print("4. Entertainment")
     print("5. Other")
     print("6. Unexpected")

    expense_choice = input("Enter your choice: ")

    if expense_choice == "1":
     amount = float(input("Enter amount: "))
     date = input("Enter date (YYYY-MM-DD): ")
     add_transaction("expense", amount, date, "Bills")


    elif expense_choice == "2":
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction("expense", amount, date, "Groceries")
    elif expense_choice == "3":
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction("expense", amount, date, "Transport")
    elif expense_choice == "4":
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction("expense", amount, date, "Entertainment")
    elif expense_choice == "5":
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction("expense", amount, date, "Other")
    elif expense_choice == "6":
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction("expense", amount, date, "Unexpected")

    else:
           print("Invalid expense option.")

           if not transactions:
               print("No transactions yet.")
           else:
               for item in transactions:
                   print(f"Date: {item['date']} | {item['category']} ({item['type']}) | ${item['amount']}")

   ##

#balance
