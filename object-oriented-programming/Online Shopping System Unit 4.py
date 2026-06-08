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
