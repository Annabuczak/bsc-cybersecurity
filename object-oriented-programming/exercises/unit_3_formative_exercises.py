# Exercise 1 – Inheritance Relationships
class Staff:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_info(self):
        print(f"{self.name} is {self.email}.")


staff1 = Staff("anna", "anna@dot.com")
staff1.show_info()


class Lecturer(Staff):
    def __init__(self, name, email, module):
        super().__init__(name, email)
        self.module = module

    def show_info(self):
        print(f"{self.name} is {self.email} and {self.module}.")


lecturer1 = Lecturer("mike", "mike@dot.com", "OOPS")
lecturer1.show_info()


class Administrator(Staff):
    def __init__(self, name, email, id_no):
        super().__init__(name, email)
        self.id_no = id_no

    def show_info(self):
        print(f"{self.name} is {self.email} and {self.id_no}.")


administrator1 = Administrator("bell", "bell@dot.com", 0)
administrator1.show_info()


# Exercise 2 – Method Overriding & Polymorphism

class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare

    def calculate_fare(self):
        return self.base_fare * 1.1


vehicle1 = Vehicle(10.0)
print(vehicle1.calculate_fare())


class Bus(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)

    def calculate_fare(self):
        return self.base_fare * 2.2


bus1 = Bus(12.0)
print(bus1.calculate_fare())


class Taxi(Vehicle):
    def __init__(self, base_fare, starting_fee, distance):
        super().__init__(base_fare)
        self.starting_fee = starting_fee
        self.distance = distance

    def calculate_fare(self):
        return self.base_fare + self.starting_fee * self.distance


taxi1 = Taxi(12.0, 10.0, 100)
print(taxi1.calculate_fare())

# Exercise 3 – Abstract Classes & “Interfaces”-Like Behaviour

import abc


class PaymentMethod(abc.ABC):
    @abc.abstractmethod
    def pay(self, amount):
        print("Payment method is implemented")


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid{amount} using card ending with <last 4 digits>.")


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid{amount} using PayPal account <email address>.")


payment1 = CardPayment()
payment2 = PayPalPayment()

payment1.pay(amount=50)
payment2.pay(amount=50)
