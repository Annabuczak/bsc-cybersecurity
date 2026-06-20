# Hospital Patient Record
from asyncio import Task


class Patient:
    def __init__(self, name, age, medical_history):
        self.name = name
        self._age = age
        self.__medical_history = medical_history

    def get_medical_summary(self):
        print(f"{self.name} sensitive medical history is hidden")

    def add_medical_note(self, note):
        self.__medical_history.append(note)


patient1 = Patient("", 26, [])
patient1.add_medical_note("My first medical note")
patient1.get_medical_summary()


# Bank Account with Safe Balance Updates
class BankAccount:

    def __init__(self, owner):
        self.__balance = 0
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


account_1 = BankAccount("Anna")
account_1.__balance = 9999  # Creates a new attribute, doesn't change the private balance
account_1.deposit(100)
print(account_1.get_balance())
account_1.withdraw(50)
print(account_1.get_balance())
