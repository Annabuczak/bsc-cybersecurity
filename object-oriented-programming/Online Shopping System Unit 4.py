# Customer class
# "The St James's Shoe Company Online Shopping System"
import datetime


class Customer:

    def __init__(self, customer_id: int, name: str, email: str, address: str) -> None:  # instance variables
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address

    # Methods for Customer class

    def register(self):
        print(f"{self.name} has registered with email {self.email}.")

    def update_details(self, name=None, email=None, address=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if address:
            self.address = address
        print(f"{self.name}'s details have been updated.")

    def place_order(self, customer_id, product_id, quantity):
        print(
            f"Customer {self.customer_id} has placed an order")

    def cancel_order(self, customer_id, product_id):
        print(
            f"Customer {self.customer_id} has canceled an order")

    def track_order(self, customer_id, product_id):
        print(
            f"Customer {self.customer_id} has received order number {product_id} tracking number xxx")


customer1 = Customer(
    1001,
    "John Smith",
    "johnsmith@example.com",
    "10 St James's Street, London"

)

customer2 = Customer(
    1002,
    "Tristian Kensington",
    "tristiankensington@example.com",
    "23 Pall Mall, London"
)

customer3 = Customer(
    1003,
    "George Cavendish",
    "georgecavendish@example.com",
    "19 Piccadilly, London"

)
customer4 = Customer(
    1004,
    " Daniel Wilton",
    "danielwilton@example.com",
    "25 Berkeley St, London"
)

customer5 = Customer(
    1005,
    "Cecil Churchill",
    "cecilchurchill@example.com",
    "9 Carlton Terrace, London"
)
customer6 = Customer(
    1006,
    "Peter Phillips",
    "peterphillips@example.com",
    "1 The Mall, London"
)

customer7 = Customer(
    1007,
    "Eric Grosvenor",
    "ericgrosvenor@example.com",
    "2 Belgrave Sq, London"
)

customer8 = Customer(
    1008,
    "James Portman",
    "jamesportman@example.com",
    "10 Waterloo Place, London"
)
customer9 = Customer(
    1009,
    "Mark Hanover",
    "markhanover@example.com",
    "77 Park Lane, London"
)
customer10 = Customer(
    1010,
    "Sebastian Windsor",
    "sebastianwindsor@example.com",
    "101 Knightsbridge, London"
)

customer1.register()
customer2.register()
customer3.register()
customer4.register()
customer5.register()
customer6.register()
customer7.register()
customer8.register()
customer9.register()
customer10.register()
customer1.update_details(email="john.new@example.com")
customer2.update_details(name="Tristian Kensington", address="45 Regent Street, London")
customer3.place_order(customer1.customer_id, customer2.customer_id, 100)
customer4.cancel_order(customer1.customer_id, customer2.customer_id)
customer5.cancel_order(customer1.customer_id, customer2.customer_id)
customer6.track_order(customer1.customer_id, customer2.customer_id)


# Class Premium Customer
class PremiumCustomer(Customer):

    def __init__(
            self,
            customer_id: int,
            name: str,
            email: str,
            address: str,
            discount_rate: float,
            membership_level: str,
            reward_points: int
    ):
        super().__init__(customer_id, name, email, address)
        self.discount_rate = discount_rate
        self.membership_level = membership_level
        self.reward_points = reward_points

    def apply_discount(self, order_value):
        discount_amount = order_value * self.discount_rate
        print(
            f"{self.name} receives a {self.discount_rate * 100}% discount "
            f"and saves £{discount_amount:.2f}."
        )

    def earn_points(self, amount_spent):
        points_earned = int(amount_spent)
        if amount_spent >= 1000:
            points_earned += 250
        self.reward_points += points_earned
        print(f"{self.name} earned {points_earned} points. Total points: {self.reward_points}")


premium_customer3 = PremiumCustomer(
    1003,
    "George Cavendish",
    "georgecavendish@example.com",
    "19 Piccadilly, London",
    0.10,
    "Gold",
    500
)

premium_customer7 = PremiumCustomer(
    1007,
    "Eric Grosvenor",
    "ericgrosvenor@example.com",
    "2 Belgrave Sq, London",
    0.15,
    "Platinum",
    1000
)

premium_customer9 = PremiumCustomer(
    1009,
    "Mark Hanover",
    "markhanover@example.com",
    "77 Park Lane, London",
    0.05,
    "Silver",
    250
)

premium_customer3.register()
premium_customer7.register()
premium_customer9.register()

premium_customer3.apply_discount(1000)
premium_customer7.apply_discount(1500)
premium_customer9.apply_discount(800)

premium_customer3.earn_points(1000)
premium_customer7.earn_points(1500)
premium_customer9.earn_points(800)


# Class shoes
class Shoes:
    def __init__(self, product_id, brand, size, colour, price, stock_quantity):
        self.product_id = product_id
        self.brand = brand
        self.size = size
        self.colour = colour
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity += quantity
        print(f"Stock updated. Current stock: {self.stock_quantity}")

    def get_details(self, product_id, brand, size, colour, price, stock_quantity):
        return f"Product ID: {self.product_id}, Brand: {self.brand}, Size: {self.size}, Colour: {self.colour}, Price: ${self.price}, Stock Quantity: {self.stock_quantity}"


shoes1 = Shoes(2001, "Cosul", 42, "Black", 940.00, 50)
shoes2 = Shoes(2002, "Shannon", 40, "Brown", 880.00, 30)
shoes3 = Shoes(2003, "Pemberly", 41, "Tan", 900.00, 20)
shoes4 = Shoes(2004, "Hampton", 43, "Navy", 920.00, 15)
shoes5 = Shoes(2005, "Balmoral", 44, "Grey", 950.00, 10)
shoes6 = Shoes(2006, "Derby", 39, "White", 870.00, 25)
shoes7 = Shoes(2007, "Oxford", 38, "Burgundy", 910.00, 5)
shoes8 = Shoes(2008, "Loafer", 37, "Green", 890.00, 8)
shoes9 = Shoes(2009, "Chelsea", 36, "Red", 930.00, 12)
shoes10 = Shoes(2010, "Monk Strap", 45, "Yellow", 940.00, 18)


class Catalogue:
    def __init__(self, catalogue_id: int, product_id: int) -> None:
        self.catalogue_id = catalogue_id
        self.product_id = product_id

    def browse(self) -> str:
        return f"Catalogue ID: {self.catalogue_id}, Product ID: {self.product_id}"

    def search_product(self) -> str:
        return f"Product ID: {self.product_id}, Catalogue ID: {self.catalogue_id}"

    def view_product_details(self) -> str:
        return f"Catalogue ID: {self.catalogue_id}, Product ID: {self.product_id}"


catalogue1 = Catalogue(3001, shoes1.product_id)
catalogue2 = Catalogue(3002, shoes2.product_id)
catalogue3 = Catalogue(3003, shoes3.product_id)
catalogue4 = Catalogue(3004, shoes4.product_id)
catalogue5 = Catalogue(3005, shoes5.product_id)
catalogue6 = Catalogue(3006, shoes6.product_id)
catalogue7 = Catalogue(3007, shoes7.product_id)
catalogue8 = Catalogue(3008, shoes8.product_id)
catalogue9 = Catalogue(3009, shoes9.product_id)
catalogue10 = Catalogue(3010, shoes10.product_id)

print(catalogue1.browse())
print(catalogue2.browse())
print(catalogue3.browse())
print(catalogue4.browse())
print(catalogue5.browse())
print(catalogue6.browse())
print(catalogue7.browse())
print(catalogue8.browse())
print(catalogue9.browse())
print(catalogue10.browse())


class Administrator:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name

    def add_product(self, product):
        self.product = product
        print(f"Admin ID: {self.admin_id}, Product ID: {product.product_id} has been added.")

    def update_stock(self, product, quantity):
        product.update_stock(quantity)
        print(f"Admin name : {self.name} updated Product ID: {product.product_id}.")

    def remove_product(self, product):
        product.update_stock(100)
        print(f"Admin name: {self.name} removed Product ID: {product.product_id}.")

    def manage_order(self, product, quantity):
        product.update_stock(quantity)
        print(
            f"Administrator {self.name} has managed an order for Product ID {product.product_id}. "
            f"Stock changed by {quantity}. Current stock: {product.stock_quantity}."
        )


administrator = Administrator(1, "Mrs Philomina Blair")
print(f"Administrator name is {administrator.name}")

administrator.add_product(shoes1)
administrator.update_stock(shoes1, 10)
administrator.remove_product(shoes2)
administrator.manage_order(shoes2, 10)
administrator.manage_order(shoes1, -1)


class Order:
    def __init__(self, order_id, order_date, order_status, total_cost):
        self.order_id = order_id
        self.order_date = order_date
        self.order_status = order_status
        self.total_cost = total_cost

    def add_product_to_the_order(self, product):
        print(f"Product ID {product.product_id} has been added to Order ID {self.order_id}.")

    def calculate_total_cost(self):
        print(f"Total Cost: {self.total_cost}")

    def cancel_order(self):
        print(f"Cancel Order ID: {self.order_id}.")

    def track_order(self):
        print(f"Track Order ID: {self.order_id}.")


order1 = Order(4001, "2026-06-10", "Pending", 940.00)
order2 = Order(4002, "2026-06-10", "Pending", 880.00)
order3 = Order(4003, "2026-06-10", "Pending", 900.00)
order4 = Order(4004, "2026-06-10", "Pending", 920.00)
order5 = Order(4005, "2026-06-10", "Pending", 950.00)

order1.add_product_to_the_order(shoes1)
order2.add_product_to_the_order(shoes2)
order3.add_product_to_the_order(shoes3)
order4.add_product_to_the_order(shoes4)
order5.add_product_to_the_order(shoes5)

order1.calculate_total_cost()
order2.calculate_total_cost()
order3.calculate_total_cost()
order4.calculate_total_cost()
order5.calculate_total_cost()

order1.cancel_order()
order2.track_order()


class Payment:
    def __init__(self, payment_id, amount, payment_status):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_status = payment_status
