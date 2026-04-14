import datetime  # handles dates
import json  # handles saving/loading data in a structured format

today_date = datetime.date.today()
print(today_date)

transactions = []  # list to store all transactions in memory


def load_data():  # loads transactions from a JSON file if it exists, otherwise starts with an empty list
    global transactions
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []  # start empty if file not found


load_data()  # run on startup


def get_valid_date():  # ensure correct date format
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Try again.")


def reset_all_data():  # delete all stored transactions
    global transactions
    confirm = input("Are you sure you want to delete ALL data? (y/n): ")

    if confirm.lower() == "y":
        transactions = []
        save_data()
        print("All data has been reset.")
    else:
        print("Cancelled.")


def delete_transaction():  # remove a selected transaction
    if not transactions:
        print("No transactions to delete.")
        return

    print("\n-- Transactions --")
    for i, t in enumerate(transactions):
        print(f"{i}: {t['category']} | £{t['amount']:.2f} | {t['date']}")

    try:
        index = int(input("Enter number to delete: "))
        removed = transactions.pop(index)
        save_data()
        print(f"Deleted: £{removed['amount']:.2f} from {removed['category']}")
    except (ValueError, IndexError):
        print("Invalid selection.")


def menu():  # main menu options
    print("\n--Financial Transactions Program--")
    print("1. Add income")
    print("2. Add expense")
    print("3. Reports")
    print("4. Balance")
    print("5. Data")
    print("6. Reset all data")
    print("7. Exit")


def add_transactions(t_type, t_amount, t_date, t_category, t_note):  # add new transaction
    transactions.append({
        "type": t_type,
        "amount": t_amount,
        "date": t_date,
        "category": t_category,
        "note": t_note if t_note.strip() else "None",  ## default note if empty
    })
    save_data()
    print(f"Success: £{t_amount:.2f} added to {t_category} on {t_date}.")


def show_balance():  # calculate and display totals
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expense
    if balance > 0:  # show status
        print("Status: Positive balance")
    elif balance < 0:
        print("Status: Overspending")
    else:
        print("Status: Balanced")

    print("\n-- Balance Summary --")
    print(f"Total Income : £{income:.2f}")
    print(f"Total Expense: £{expense:.2f}")
    print(f"Net Balance  : £{balance:.2f}")


def monthly_summary():  # summary for current month
    if len(transactions) == 0:
        print("No transactions added.")
        return

    current_month_prefix = datetime.date.today().strftime("%Y-%m")
    total_income = 0.0
    total_expense = 0.0

    for t in transactions:
        if str(t["date"]).startswith(current_month_prefix):  # filter by month
            if t["type"] == "income":
                total_income += t["amount"]
            elif t["type"] == "expense":
                total_expense += t["amount"]

    net_balance = total_income - total_expense

    print("\n--Monthly Summary--")
    print(f"Total Income: £{total_income:.2f}")
    print(f"Total Expense: £{total_expense:.2f}")
    print(f"Net Balance: £{net_balance:.2f}")


def category_summary():  # totals per category
    if len(transactions) == 0:
        print("No transactions added.")
        return

    income_totals = {}
    expense_totals = {}

    for t in transactions:
        cat = t["category"]
        amount = t["amount"]

        if t["type"] == "income":
            income_totals[cat] = income_totals.get(cat, 0) + amount
        elif t["type"] == "expense":
            expense_totals[cat] = expense_totals.get(cat, 0) + amount

    print("\nIncome by category:")
    if not income_totals:
        print("  No income recorded.")
    else:
        for cat, total in income_totals.items():
            print(f"  - {cat}: £{total:.2f}")

    print("\nExpense by category:")
    if not expense_totals:
        print("  No expense recorded.")
    else:
        for cat, total in expense_totals.items():
            print(f"  - {cat}: £{total:.2f}")


def highest_lowest_expense():  # find highest and lowest expense categories
    expense_totals = {}

    for t in transactions:
        if t["type"] == "expense":
            cat = t["category"]
            expense_totals[cat] = expense_totals.get(cat, 0) + t["amount"]

    if not expense_totals:
        print("No expense data available.")
        return

    highest = max(expense_totals, key=expense_totals.get)
    lowest = min(expense_totals, key=expense_totals.get)

    print(f"\nHighest expense: {highest} (£{expense_totals[highest]:.2f})")
    print(f"Lowest expense: {lowest} (£{expense_totals[lowest]:.2f})")


def search_transactions():  # search/filter transactions
    if len(transactions) == 0:
        print("No transactions added.")
        return

    print("\n-- 🔎 Filter Transactions --")
    target_month = input("Enter month (YYYY-MM) or press Enter for all: ").strip()
    target_category = input("Enter category (e.g., Groceries) or press Enter for all: ").strip()

    print("\n-- Search Results --")
    found_any = False

    for t in transactions:
        match_month = (target_month == "") or str(t["date"]).startswith(target_month)
        match_category = (target_category == "") or (t["category"].lower() == target_category.lower())

        if match_month and match_category:
            print(f"[{t['date']}] {t['type'].capitalize()} | {t['category']} | £{t['amount']:.2f} | Note: {t['note']}")
            found_any = True

    if not found_any:
        print("No transactions found matching those filters.")


def save_data():  # save transactions to file
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)


while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            print("\n-- Add Income --")
            print("1. Salary")
            print("2. Freelance")
            print("3. Other")
            print("4. Exit to main menu")

            income_choice = input("Enter your choice: ")

            if income_choice == "4":
                print("Returning to main menu...")
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

            while True:
                try:
                    amount = float(input("Enter amount: "))
                    break
                except ValueError:
                    print("Invalid number. Please enter digits only. Try again.")

            date_choice = input("Do you want to use today's date? (y/n): ").strip().lower()
            if date_choice == "y":
                date = datetime.date.today().strftime("%Y-%m-%d")
            else:
                date = get_valid_date()  # FIX: reused your function

            note = input("Enter a note (or press Enter to skip): ")

            add_transactions("income", amount, date, category, note)

    elif choice == "2":
        while True:
            print("\n-- Add Expense --")
            print("1. Bills")
            print("2. Groceries")
            print("3. Transport")
            print("4. Entertainment")
            print("5. Other")
            print("6. Exit to main menu")

            expense_choice = input("Enter your choice: ")

            if expense_choice == "6":
                print("Returning to main menu...")
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

            while True:
                try:
                    amount = float(input("Enter amount: "))
                    break
                except ValueError:
                    print("Invalid number. Please enter digits only. Try again.")

            date_choice = input("Do you want to use today's date? (y/n): ").strip().lower()
            if date_choice == "y":
                date = datetime.date.today().strftime("%Y-%m-%d")
            else:
                date = get_valid_date()  # FIX

            note = input("Enter a note (or press Enter to skip): ")

            add_transactions("expense", amount, date, category, note)

    elif choice == "3":
        while True:
            print("\n-- Reports Menu --")
            print("1. Monthly Summary")
            print("2. Total Income")
            print("3. Total Expense")
            print("4. Net Balance")
            print("5. Category Breakdown")
            print("6. Highest & Lowest Expense")
            print("7. Go to main menu")

            reports_choice = input("Enter your choice: ")

            if reports_choice == "7":
                break
            elif reports_choice == "1":
                monthly_summary()
            elif reports_choice == "2":
                t_income = sum(t["amount"] for t in transactions if t["type"] == "income")
                print(f"\nTotal Income: £{t_income:.2f}")
            elif reports_choice == "3":
                t_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
                print(f"\nTotal Expense: £{t_expense:.2f}")
            elif reports_choice == "4":
                show_balance()
            elif reports_choice == "5":
                category_summary()
            elif reports_choice == "6":
                highest_lowest_expense()
            else:
                print("Invalid choice. Try again.")

    elif choice == "4":
        show_balance()

    elif choice == "5":
        while True:
            print("\n-- Data Menu --")
            print("1. Search")
            print("2. Delete")
            print("3. Back")

            data_choice = input("Enter choice: ")
            if data_choice == "1":
                search_transactions()
            elif data_choice == "2":
                delete_transaction()
            elif data_choice == "3":
                break
            else:
                print("Invalid choice.")

    elif choice == "6":
        reset_all_data()
    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
