transactions = []


def menu():
    print("\n--Financial Transactions Program--")
    print("1. Add income")
    print("2. Add expense")
    print("3. Reports")
    print("4. Balance")
    print("5. Data")
    print("6. Go to main menu")


def add_transactions(t_type, t_amount, t_date, t_category):
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
    menu()

    choice = input("Enter your choice: ")
    while True:
        if choice == "1":
            print("1. Salary")
            print("2. Freelance")
            print("3. Other")
            print("4. Exit to main menu")

            income_choice = input("Enter your choice: ")

            if income_choice == "1":
                amount = float(input("Enter amount: "))
                date = input("Enter date (dd/mm/yyyy): ")
                add_transactions("income", amount, date, "Salary")

            elif income_choice == "2":
                amount = float(input("Enter amount: "))
                date = input("Enter date (dd/mm/yyyy): ")
                add_transactions("income", amount, date, "Freelance")

            elif income_choice == "3":
                amount = float(input("Enter amount: "))
                date = input("Enter date (dd/mm/yyyy): ")
                add_transactions("income", amount, date, "Other")

            elif income_choice == "4":
                print("Go to main menu")
            break


        elif choice == "2":
            print("1. Bills")
            print("2. Groceries")
            print("3. Transport")
            print("4. Entertainment")
            print("5. Other")
            print("6. Exit to main menu")

            expense_choice = input("Enter your choice: ")
    while True:
        if expense_choice == "1":
            amount = float(input("Enter amount: "))
            date = input("Enter date (dd/mm/yyyy): ")
            add_transactions("expense", amount, date, "Bills")


        elif expense_choice == "2":
            amount = float(input("Enter amount: "))
            date = input("Enter date (dd/mm/yyyy): ")
            add_transactions("expense", amount, date, "Groceries")
        elif expense_choice == "3":
            amount = float(input("Enter amount: "))
            date = input("Enter date (dd/mm/yyyy): ")
            add_transactions("expense", amount, date, "Transport")
        elif expense_choice == "4":
            amount = float(input("Enter amount: "))
            date = input("Enter date (dd/mm/yyyy): ")
            add_transactions("expense", amount, date, "Entertainment")
        elif expense_choice == "5":
            amount = float(input("Enter amount: "))
            date = input("Enter date (dd/mm/yyyy): ")
            add_transactions("expense", amount, date, "Other")

        else:
            expense_choice == "6"
            print("Go to main menu")
        break
