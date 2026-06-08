class Shoes
    def __init__(self, product_id, brand, size, colour,price, stock_quantity):
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

shoes1 = Shoes(2001, "Cosul R1", 42, "Black", 940.00, 50)
shoes2 = Shoes(2002, "Shannon", 40, "Brown", 880.00, 30)
shoes3 = Shoes(2003, "Pemberly", 41, "Tan", 900.00, 20)
shoes4 = Shoes(2004, "Hampton", 43, "Navy", 920.00, 15)
shoes5 = Shoes(2005, "Balmoral", 44, "Grey", 950.00, 10)
shoes6 = Shoes(2006, "Derby", 39, "White", 870.00, 25)
shoes7  = Shoes(2007, "Oxford", 38, "Burgundy", 910.00, 5)
shoes8 = Shoes(2008, "Loafer", 37, "Green", 890.00, 8)
shoes9 = Shoes(2009, "Chelsea", 36, "Red", 930.00, 12)
shoes10 = Shoes(2010, "Monk Strap", 45, "Yellow", 940.00, 18)

