"""Small examples for practising testing and debugging."""


def calculate_total(price, quantity):
    """Return the total cost for a quantity of items."""
    return price * quantity


def apply_discount(price, discount_percent):
    """Apply a percentage discount to a price."""
    discount = price * (discount_percent / 100)
    return price - discount


class BankAccount:
    """Simple bank account used for unit-test examples."""

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


class Task:
    """Simple to-do task used for object testing examples."""

    def __init__(self, name):
        self.name = name
        self.done = False

    def mark_done(self):
        self.done = True


def run_examples():
    print(calculate_total(10, 5))
    print(apply_discount(100, 10))

    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    print(account.balance)

    task = Task("Finish OOP")
    task.mark_done()
    print(task.name, task.done)


def check_age(age):
    if age < 18:
        raise ValueError("User must be 18 or over")

    return True


age = 15

import pytest
from age_checker import check_age


def test_check_age_returns_true_for_adult():
    assert check_age(18) is True


def test_check_age_raises_error_for_child():
    with pytest.raises(ValueError):
        check_age(15)
