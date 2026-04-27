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


def take_item(current_room, rooms, inventory):
    item = rooms[current_room]["item"]

    if item is None:
        print("There is nothing to take here.")
        return

    if item in inventory:
        print("You already have this item.")
        return

    inventory.append(item)
    rooms[current_room]["item"] = None

    print(f"You picked up {item}.")
    print("Inventory", inventory)


def drop_item(inventory, portal_items, current_room):
    if current_room != "The Sanctuary":
        print("You can only drop items in the Sanctuary.")
        return

    if not inventory:
        print("You have nothing to drop.")
        return

    print("Your inventory:", inventory)
    item = input("Which item do you want to drop? ").strip()

    required_items = ["Letter", "Photo", "Pen", "Book", "Newspaper"]

    if item in inventory:
        inventory.remove(item)
        portal_items.append(item)
        print(f"You placed {item} into the portal.")

        if all(i in portal_items for i in required_items):
            print("The portal awakens... The Golden Key appears.")
    else:
        print("You don't have that item.")
