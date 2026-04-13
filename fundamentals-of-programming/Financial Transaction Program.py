# Built-in libraries used for saving date (datetime) and data (json)
import datetime
import json

today_date = datetime.date.today()  # Display today's date when program starts
print(today_date)  # print today's date to the user

transactions = []  # List to store all transactions in memory


def get_valid_date():  # This function ensures user enters date in correct format (YYYY-MM-DD)
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")  # Prompt user for date input
        try:
            datetime.datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:  # If invalid format, show error and ask again
            print("Invalid date format. Try again.")


def load_data():  # This function loads transactions from a JSON file when the program starts. If the file doesn't exist, it starts with empty list
    global transactions  # Allow modification of the global transactions list
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:  # If the file doesn't exist, start with an empty list
        transactions = []


load_data()  # Load existing data from file when program starts


def reset_all_data():  # This function allows the user to reset all data by clearing the transactions list and saving the empty list to the file. It asks for confirmation before doing so.
    global transactions
    confirm = input("Are you sure you want to delete ALL data? (y/n): ")

    if confirm.lower() == "y":  # If user confirms, clear transactions and save empty list to file
        transactions = []  # Clear the transactions list
        save_data()  # Save the empty list to the file, effectively resetting all data
        print("All data has been reset.")
    else:
        print("Cancelled.")


def save_data():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)


def add_transactions(t_type, t_amount, t_date, t_category, t_note):
    transactions.append({
        "type": t_type,
        "amount": t_amount,
        "date": t_date,
        "category": t_category,
        "note": t_note,
    })
    save_data()
    print(f"Success: £{t_amount:.2f} added to {t_category} on {t_date}.")


def delete_transaction():
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


def show_balance():
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expense

    print("\n-- Balance Summary --")
    print(f"Total Income : £{income:.2f}")
    print(f"Total Expense: £{expense:.2f}")
    print(f"Net Balance  : £{balance:.2f}")


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
            elif t["type"] == "expense":
                total_expense += t["amount"]

    net_balance = total_income - total_expense

    print("\n--Monthly Summary--")
    print(f"Total Income: £{total_income:.2f}")
    print(f"Total Expense: £{total_expense:.2f}")
    print(f"Net Balance: £{net_balance:.2f}")


def category_summary():
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
    for cat, total in income_totals.items():
        print(f"  - {cat}: £{total:.2f}")

    print("\nExpense by category:")
    for cat, total in expense_totals.items():
        print(f"  - {cat}: £{total:.2f}")


def highest_lowest_expense():
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


def search_transactions():
    if len(transactions) == 0:
        print("No transactions added.")
        return

    print("\n-- 🔎 Filter Transactions --")
    target_month = input("Enter month (YYYY-MM) or press Enter for all: ").strip()
    target_category = input("Enter category or press Enter for all: ").strip()

    print("\n-- Search Results --")
    found_any = False

    for t in transactions:
        match_month = (target_month == "") or str(t["date"]).startswith(target_month)
        match_category = (target_category == "") or (t["category"].lower() == target_category.lower())

        if match_month and match_category:
            print(f"[{t['date']}] {t['type']} | {t['category']} | £{t['amount']:.2f}")
            found_any = True

    if not found_any:
        print("No transactions found.")


def menu():
    print("\n--Financial Transactions Program--")
    print("1. Add income")
    print("2. Add expense")
    print("3. Reports")
    print("4. Balance")
    print("5. Data")
    print("6. Reset all data")
    print("7. Exit")


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter income category: ")
        amount = float(input("Enter amount: "))
        date = get_valid_date()
        note = input("Enter note: ")
        add_transactions("income", amount, date, category, note)

    elif choice == "2":
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: "))
        date = get_valid_date()
        note = input("Enter note: ")
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
            print("7. Back")

            reports_choice = input("Enter choice: ")

            if reports_choice == "1":
                monthly_summary()
            elif reports_choice == "2":
                print(sum(t["amount"] for t in transactions if t["type"] == "income"))
            elif reports_choice == "3":
                print(sum(t["amount"] for t in transactions if t["type"] == "expense"))
            elif reports_choice == "4":
                show_balance()
            elif reports_choice == "5":
                category_summary()
            elif reports_choice == "6":
                highest_lowest_expense()
            elif reports_choice == "7":
                break
            else:
                print("Invalid choice.")

    elif choice == "4":
        show_balance()

    elif choice == "5":
        search_transactions()

    elif choice == "6":
        reset_all_data()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
