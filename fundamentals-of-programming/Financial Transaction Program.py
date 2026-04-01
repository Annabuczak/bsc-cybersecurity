transactions = []

def show_menu():
    print("\n--Financial Transaction Program--")
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View balance")
def add_transaction(t_type, t_amount, t_date, t_category):
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
            print("Invalid income option")
    else:
        print("Invalid input. Please choose 1-4.")


