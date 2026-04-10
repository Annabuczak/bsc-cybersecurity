import datetime

datetime.date.today()
today_date = datetime.date.today()
print(today_date)

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

    if choice == "1":
        while True:
            print("1. Salary")
            print("2. Freelance")
            print("3. Other")
            print("4. Exit to main menu")

            income_choice = input("Enter your choice: ")
            if income_choice == "4":
                print("Go to main menu")
                break
            if income_choice == "1":
                category = "Salary"
            elif income_choice == "2":
                category = "Freelance"
            elif income_choice == "3":
                category = "Other"
            else:
                print("Invalid choice. Try again.")
                continue
            add_transactions("income", amount, today_date, category)
            amount = float(input("Enter amount: "))
            date_choice = input("Do you want to use today's date? (y/n): ").strip().lower()



    elif choice == "2":
        while True:
            print("1. Bills")
            print("2. Groceries")
            print("3. Transport")
            print("4. Entertainment")
            print("5. Other")
            print("6. Exit to main menu")

            expense_choice = input("Enter your choice: ")
            if expense_choice == "6":
                print("Go to main menu")
                break
            if expense_choice == "1":
                category = "Bills"
            elif expense_choice == "2":
                category = "Groceries"
            elif expense_choice == "3":
                category = "Transport"
            elif expense_choice == "4":
                category = "Entertainment"
            elif expense_choice == "5":
                category = "Other"
            else:
                print("Invalid choice. Try again.")
                continue
            add_transactions("expenses", amount, today_date, category)
            amount = float(input("Enter amount: "))
            date_choice = input("Do you want to use today's date? (y/n): ").strip().lower()
