def calculate_total(price, quantity):
    return price + quantity


price = 10
quantity = 5
total = calculate_total(price, quantity)
print(total)


# from shop.py
def calculate_total(price, quantity):
    return price * quantity


price = 10
quantity = 5
total = calculate_total(price, quantity)
print(total)
# test
from shop import calculate_total


def test_calculate_total():
    assert calculate_total(10, 5) == 50


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


from bank_account import BankAccount


def test_deposit_increases_balance():
    account = BankAccount(100)
    account.deposit(50)
    assert account.balance == 150


def test_withdraw_reduces_balance():
    account = BankAccount(100)
    account.withdraw(30)
    assert account.balance == 70


# A test usually looks like this:
def test_something_should_happen():
    object = Something()

    object.do_something()

    assert object.value == expected_result


# rise error import pytest

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


account = BankAccount(100)
account.withdraw(200)
print(account.balance)
account.deposit(200)
print(account.balance)

from bank_account import BankAccount


def test_withdraw_too_much_raises_error():
    account = BankAccount(100)

    with pytest.raises(ValueError):
        account.withdraw(200)


def apply_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount


price = 100
discount_percent = 10
print(apply_discount(price, discount_percent))

from discount import apply_discount


def test_apply_discount_takes_10_percent_off():
    assert apply_discount(100, 10) == 90


def test_apply_discount_takes_50_percent_off():
    assert apply_discount(80, 50) == 40


# test an object
class Task:
    def __init__(self, name):
        self.name = name
        self.done = False

    def mark_done(self):
        self.done = True


name = "Anna"
task = Task(name)
print(task.name)
task.mark_done()
print(task.done)

from todo import Task


def test_task_starts_not_done():
    task = Task("Finish OOP")
    assert task.done == False


def test_mark_done_changes_done_to_true():
    task = Task("Finish OOP")
    task.mark_done()
    assert task.done == True


def apply_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount


price = 100
discount_percent = 10
print(apply_discount(price, discount_percent))

from discount import apply_discount


def test_apply_discount_takes_10_percent_off():
    assert apply_discount(100, 10) == 90


def test_apply_discount_takes_50_percent_off():
    assert apply_discount(80, 50) == 40


def calculate_shipping(order_total):
    if order_total > 50:
        return 0
    else:
        return 4.99


from shipping import calculate_shipping


def test_shipping_is_free_when_order_is_over_50():
    assert calculate_shipping(60) == 0


def test_shipping_is_free_when_order_is_exactly_50():
    assert calculate_shipping(50) == 0


def test_shipping_costs_4_99_when_order_is_under_50():
    assert calculate_shipping(20) == 4.99
