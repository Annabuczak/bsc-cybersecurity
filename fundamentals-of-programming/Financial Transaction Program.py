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


def save_data():  # This function saves the current transactions list to a JSON file. It is called whenever a transaction is added or deleted to ensure data persistence.
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)  # Save the transactions list to the file in JSON format


def add_transactions(t_type, t_amount, t_date, t_category,
                     t_note):  # This function adds a new transaction to the transactions list. It takes the type (income or expense), amount, date, category, and note as parameters. After adding the transaction to the list, it calls save_data() to save the updated list to the file.
    transactions.append({
        "type": t_type,
        "amount": t_amount,
        "date": t_date,
        "category": t_category,
        "note": t_note,
    })
    save_data()  # Save the updated transactions list to the file after adding a new transaction
    print(f"Success: £{t_amount:.2f} added to {t_category} on {t_date}.")


def delete_transaction():  # This function allows the user to delete a transaction from the transactions list. It first checks if there are any transactions to delete. If there are, it displays them with an index number. The user can then enter the index number of the transaction they want to delete. The function removes the selected transaction from the list and saves the updated list to the file. If the user enters an invalid index, it shows an error message.
    if not transactions:
        print("No transactions to delete.")
        return  # If there are no transactions, inform the user and exit the function

    print("\n-- Transactions --")  # Display the list of transactions with index numbers for the user to select from
    for i, t in enumerate(
            transactions):  # Loop through the transactions and print each one with its index number, category, amount, and date
        print(f"{i}: {t['category']} | £{t['amount']:.2f} | {t['date']}")

    try:
        index = int(input("Enter number to delete: "))
        removed = transactions.pop(
            index)  # Remove the selected transaction from the list using the index provided by the user
        save_data()  # Save the updated transactions list to the file after deleting a transaction
        print(f"Deleted: £{removed['amount']:.2f} from {removed['category']}")
    except (ValueError, IndexError):  # Handle invalid input or index errors
        print("Invalid selection.")


def show_balance():  # This function calculates and displays the total income, total expense, and net balance. It sums up all transactions of type "income" and "expense" separately, then calculates the net balance by subtracting total expenses from total income. Finally, it prints the results in a formatted manner.
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expense

    print("\n-- Balance Summary --")
    print(f"Total Income : £{income:.2f}")
    print(f"Total Expense: £{expense:.2f}")
    print(f"Net Balance  : £{balance:.2f}")


def monthly_summary():  # This function generates a summary of transactions for the current month. It first checks if there are any transactions to summarize. If there are, it calculates the total income and total expenses for the current month by checking if the transaction date starts with the current month prefix (YYYY-MM). It then calculates the net balance for the month and prints the results in a formatted manner.
    if len(transactions) == 0:  # Check if there are any transactions to summarize. If not, inform the user and exit the function
        print("No transactions added.")
        return

    current_month_prefix = datetime.date.today().strftime("%Y-%m")  #
    total_income = 0.0
    total_expense = 0.0

    for t in transactions:
        if str(t["date"]).startswith(current_month_prefix):
            if t["type"] == "income":
                total_income += t["amount"]
            elif t["type"] == "expense":
                total_expense += t["amount"]

    net_balance = total_income - total_expense  # Calculate net balance for the month by subtracting total expenses from total income

    print("\n--Monthly Summary--")
    print(f"Total Income: £{total_income:.2f}")
    print(f"Total Expense: £{total_expense:.2f}")
    print(f"Net Balance: £{net_balance:.2f}")


def category_summary():  # This function generates a summary of transactions by category. It first checks if there are any transactions to summarize. If there are, it iterates through the transactions and sums up the amounts for each category separately for income and expenses. It then prints the total income and total expenses for each category in a formatted manner.
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


def highest_lowest_expense():  # This function identifies and displays the highest and lowest expense categories. It first checks if there are any transactions to analyze. If there are, it iterates through the transactions and sums up the expenses for each category. It then finds the category with the highest total expense and the category with the lowest total expense, and prints the results in a formatted manner.
    expense_totals = {}

    for t in transactions:  # Iterate through the transactions and sum up the expenses for each category. If the transaction type is "expense", it adds the amount to the corresponding category in the expense_totals dictionary.
        if t["type"] == "expense":
            cat = t["category"]
            expense_totals[cat] = expense_totals.get(cat, 0) + t["amount"]

    if not expense_totals:  # Check if there are any expenses to analyze. If not, inform the user and exit the function
        print("No expense data available.")
        return

    highest = max(expense_totals, key=expense_totals.get)
    lowest = min(expense_totals, key=expense_totals.get)

    print(f"\nHighest expense: {highest} (£{expense_totals[highest]:.2f})")
    print(f"Lowest expense: {lowest} (£{expense_totals[lowest]:.2f})")


def search_transactions():  # This function allows the user to search for transactions based on month and/or category. It first checks if there are any transactions to search through. If there are, it prompts the user to enter a month (in YYYY-MM format) and a category (or press Enter to search for all). It then iterates through the transactions and checks if each transaction matches the specified month and category criteria. If a transaction matches, it is printed in a formatted manner. If no transactions match the criteria, it informs the user that no transactions were found.
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


def menu():  # This function displays the main menu options to the user. It is called in a loop to continuously show the menu after each action until the user chooses to exit. The menu includes options for adding income, adding expenses, viewing reports, checking balance, searching data, resetting all data, and exiting the program.
    print("\n--Financial Transactions Program--")
    print("1. Add income")
    print("2. Add expense")
    print("3. Reports")
    print("4. Balance")
    print("5. Data")
    print("6. Reset all data")
    print("7. Exit")


while True:  # Main program loop that continuously shows the menu and processes user input until the user chooses to exit. It calls the appropriate functions based on the user's choice and handles invalid input by showing an error message.
    menu()  # Display the main menu options to the user
    choice = input("Enter your choice: ")

    if choice == "1":  #
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
