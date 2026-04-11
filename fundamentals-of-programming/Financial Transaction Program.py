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


def add_transactions(t_type, t_amount, t_date, t_category, t_note, ):
    transactions.append({
        "type": t_type,
        "amount": t_amount,
        "date": t_date,
        "category": t_category,
        "note": t_note,
    })

    print(f"Success: £{t_amount} added to {t_category} on {t_date}.")


def show_balance(t_type, t_amount, t_date, t_category, t_note, ):
    transactions.append({
        "type": t_type,
        "amount": t_amount,
        "date": t_date,
        "category": t_category,
        "note": t_note,
    })
    print(f"Success: £{t_amount} added to {t_category} on {t_date}.")


def monthly_summary():
    if len(transactions) == 0:
        print("No transactions added.")
        return

    current_month_prefix = datetime.date.today().strftime("%Y-%m")
    total_income = 0.0
    total_expense = 0.0

    for t in transactions:
        if str(t["date"]).startswith(current_month_prefix):
            if t["type"] == "income":
                total_income += t["amount"]
            elif t["type"] == "expenses":
                total_expense += t["amount"]

    net_balance = total_income - total_expense

    print("\n--Monthly Summary--")
    print(f"Total Income: £{total_income}")
    print(f"Total Expense: £{total_expense}")
    print(f"Net Balance: £{net_balance}")


def category_summary():
    if len(transactions) == 0:
        print("No transactions added.")
        return

    total_income = 0.0
    total_expense = 0.0

    for t in transactions:
        category.append(t["category"])
    amount = t["amount"]
    if t["type"] == "income":
        total_income += amount
    elif t["type"] == "expenses":
        total_expense += amount
    print("\nIncome by category:")
    if len(total_income) == 0:
        print("  No income recorded.")
    else:
        for cat, total in total_income.items():
            print(f"  - {cat}: ${total:.2f}")
        print("\n Expense by category:")
        if len(total_expense) == 0:
            print("  No income recorded.")
        else:
            for cat, total in total_expense.items():
                print(f"  - {cat}: ${total:.2f}")


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
            amount = len(input("Enter amount: "))

            date_choice = input("Do you want to use today's date? (y/n): ").strip().lower()
            if date_choice == "y":
                date = datetime.date.today()
            else:
                date = input("Enter date (YYYY-MM-DD): ")
            note = input("Enter a note (or press Enter to skip): ")
            if note.strip() == "":
                note = "None"
            add_transactions("income", amount, date, category, note, )

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
            amount = len(input("Enter amount: "))

            date_choice = input("Do you want to use today's date? (y/n): ").strip().lower()
            if date_choice == "y":
                date = datetime.date.today()
            else:
                date = input("Enter date (YYYY-MM-DD): ")
            note = input("Enter a note (or press Enter to skip): ")
            if note.strip() == "":
                note = "None"
            add_transactions("expenses", amount, date, category, note, )


    elif choice == "3":
        while True:
            print("1. Monthly Summary")
            print("2. Total Income: £")
            print("3. Total Expense: £")
            print("4. Net Balance: £")
            print("5. Go to main menu")

            reports_choice = input("Enter your choice: ")
            if reports_choice == "6":
                print("Go to main menu")
            break

        if reports_choice == "1":
            monthly_summary()
        elif reports_choice in ["2", "3", "4"]:
            t_income = sum(t["amount"] for t in transactions if t["type"] == "income")
            t_expense = sum(t["amount"] for t in transactions if t["type"] == "expenses")
        if reports_choice == "2":
            print(f"\nTotal Lifetime Income: £{t_income:.2f}")
        elif reports_choice == "3":
            print(f"\nTotal Lifetime Expense: £{t_expense:.2f}")
        elif reports_choice == "4":
            print(f"\nTotal Net Balance: £{t_income - t_expense:.2f}")
        else:
            print("Invalid choice. Try again.")
