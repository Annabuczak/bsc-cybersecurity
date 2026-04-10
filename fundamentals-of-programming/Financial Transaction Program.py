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
