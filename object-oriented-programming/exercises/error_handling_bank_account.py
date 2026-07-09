class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.__balance:
            raise InsufficientFundsError("Not enough funds for this withdrawal.")

        self.__balance -= amount

    def get_balance(self):
        return self.__balance


account_1 = BankAccount(0)

try:
    account_1.deposit(10)
    account_1.withdraw(100)
except ValueError as e:
    print("Error:", e)
except InsufficientFundsError as e:
    print("Error:", e)

print("Balance:", account_1.get_balance())
