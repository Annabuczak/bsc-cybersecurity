# Customer class
# "The St James's Shoe Company Online Shopping System"
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

    def place_order(self):
        print(
            f"{self.customer_id} has placed an order for {self.product_id} in {self.size} number of units {self.quantity}.")


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

    def get_details(self):
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
