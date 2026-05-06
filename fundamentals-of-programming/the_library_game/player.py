from inventory import Inventory


class Player:
    def __init__(self, name="Sebastian"):
        self.name = name
        self.current_room = "The Sanctuary"
        self.inventory = Inventory()

    def has_item(self, item_name):
        return self.inventory.has_item(item_name)

    def show_inventory(self):
        self.inventory.display()
