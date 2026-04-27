class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1
        print(self.inventory)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory[item] -= 1
            if self.inventory[item] == 0:
                del self.inventory[item]
        else:
            print("Item not found")

    def display(self):
        if not self.inventory:
            print("Inventory is empty")
        else:
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")

    def get_inventory(self):
        return self.inventory
