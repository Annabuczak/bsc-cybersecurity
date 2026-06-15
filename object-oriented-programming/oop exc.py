class BankAccount:
    def __init__(self, owner, balance, deposit, withdrawal):
        self.owner = owner
        self.balance = balance
        self.deposit = deposit
        self.withdrawal = withdrawal

    def account_users(self):
        print(
            f"Account holder {self.owner}, has  {self.balance}, after paying in {self.deposit},and taking out  {self.withdrawal}")
        return self.balance + self.deposit - self.withdrawal

    def calculate_balance(self):
        return self.balance + self.deposit - self.withdrawal

    def withdraw(self, balance):
        if balance > 100:
            print("You don't have enough money!")
        else:
            print("You have enough money!")


account_user1 = BankAccount("John", 20000, 10000, 110)
account_user2 = BankAccount("Anna", 40000, 1003, 90)
account_user1.account_users()
account_user2.account_users()
account_user1.withdraw(110)
account_user2.withdraw(9)
account_user1.account_users()
print(account_user1.account_users())
print(account_user2.account_users())
print(account_user1.withdraw(110))
print(account_user2.withdraw(90))
