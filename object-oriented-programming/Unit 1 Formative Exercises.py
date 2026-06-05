class Member:
    def __init__(self, name, membership_type, is_active):
        self.name = name
        self.membership_type = membership_type
        self.is_active = is_active

    def describe(self):
        print(f"{self.name} is on a {self.membership_type} membership. Active: {self.is_active}")


member_one = Member("John", "Gold", True)
member_two = Member("Anna", "Silver", False)
member_three = Member("Lou", "Platinum", True)

members = [member_one, member_two, member_three]

for member in members:
    member.describe()

info = {
    "name": "",
    "price": 0.00,
    "quantity": 0,
}

name = input("Name of the item? ")
price = float(input("Price of the item? "))
quantity = int(input("Quantity of the item? "))

info["name"] = name
info["price"] = price
info["quantity"] = quantity

cart = [info]


def total(cart):
    total_price = 0

    for item in cart:
        total_price = total_price + item["price"] * item["quantity"]

    return total_price


print(info)
print(total(cart))


class Cart_items:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity


class Shopping_cart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, item_name, price, quantity):
        item = Cart_items(item_name, price, quantity)
        self.cart_items.append(item)

    def calculate_total(self):
        total_price = 0

        for item in self.cart_items:
            total_price = total_price + item.price * item.quantity

        return total_price


item_name = input("Item name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

shopping_cart = Shopping_cart()
shopping_cart.add_item(item_name, price, quantity)

total_price = shopping_cart.calculate_total()
print(total_price)

students = [
    {"name": "John Sawyer", "grade": 45},
    {"name": "Anna Buczak", "grade": 85},
    {"name": "Lou Costa", "grade": 50},
    {"name": "Dina Gordon", "grade": 88},
    {"name": "Arlo Gordon", "grade": 39}
]

print(students)

total = 0
passed_students = []

for student in students:
    total += student["grade"]

    if student["grade"] >= 50:
        passed_students.append(student["name"])

average = total / len(students)

print("Average grade:", average)
print("Students who passed:", passed_students)
