class BankAccount():
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            self.__balance -= amount
            print("Withdraw amount =", amount)


account_1 = BankAccount(0)
deposit = account_1.deposit(10)
withdraw = account_1.withdraw(100)
balance = BankAccount

try:
    account_1.deposit(0)
    account_1.withdraw(100)
except ValueError as e:
    print("error: ", e)
except InsufficientFundsError as e:
    print("error: ", e)

print("Balance: ", balance)
