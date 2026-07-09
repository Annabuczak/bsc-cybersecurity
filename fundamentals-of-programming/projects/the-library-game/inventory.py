class Inventory:
    # Manages the player's items and quantities
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        # Add a new item or increase its count if already owned
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1

    def remove_item(self, item):
        # Decrease item count, and remove it completely if it hits 0
        if item in self.inventory:
            self.inventory[item] -= 1
            if self.inventory[item] == 0:
                del self.inventory[item]

    def has_item(self, item_name):
        return item_name in self.inventory

    def display(self):
        # Print all items to the screen
        if not self.inventory:
            print("Inventory is empty")
        else:
            for item, qty in self.inventory.items():
                print(f"- {item}: {qty}")


# Takes item from the portal
def take_item(current_room, rooms, inventory):
    # Pick up an item from the room, preventing duplicates
    item = rooms[current_room].get("item")

    if item is None:
        print("There is nothing to take here.")
        return

    if item in inventory.inventory:
        print("You already have this item.")
        return

    inventory.add_item(item)
    rooms[current_room]["item"] = None
    print(f"You picked up {item}.")


# Drops items in the portal
def drop_item(inventory, portal_items, current_room):
    # Sacrifice items to the portal in the Sanctuary
    if current_room != "The Sanctuary":
        print("You can only drop items in the Sanctuary.")
        return

    if not inventory.inventory:
        print("You have nothing to drop.")
        return

    print("Your inventory:")
    inventory.display()

    item = input("Which item do you want to drop? ").strip().title()
    required_items = ["Letter", "Photo", "Pen", "Book", "Newspaper"]

    if item in inventory.inventory:
        inventory.remove_item(item)
        portal_items.append(item)
        print(f"You placed {item} into the portal.")

        # Check for the endgame unlock condition
        if all(i in portal_items for i in required_items):
            print("The portal awakens... The Golden Key appears.")
    else:
        print("You don't have that item.")


# Examine items

def examine_items(inventory):
    # Read the narrative lore attached to specific items
    if not inventory.inventory:
        print("\nYour pockets are empty. You have nothing to examine.")
        return

    print("\nYour current inventory:")
    inventory.display()

    choice = input("Which item do you want to examine? (or type 'none'): ").strip()

    if choice.lower() == "none":
        return

    matching_item = None
    for item in inventory.inventory:
        if item.lower() == choice.lower():
            matching_item = item
            break

    choice = matching_item

    if choice not in inventory.inventory:
        print("\nYou don't have that item.")
        return

    print(f"\nExamining... {choice}:")

    if choice == "Letter":
        print("\nThe paper is brittle. The handwriting is hurried, almost desperate...")
        print("\"My dearest Penelope...They know. We cannot wait any longer.")
        print("Meet me at the Estació de Sants, last train leaves just before midnight.")
        print("If I do not see you, I will assume you changed your mind.")
        print("With undying love. J.C\"")
        print("A dark, dried stain covers the bottom corner.")

    elif choice == "Photo":
        print("\nIt is half of a torn black-and-white photo.")
        print("A young woman with long, dark hair smiles at someone out of frame.")
        print("She wears a white wedding dress. Her eyes are full of fear.")

    elif choice == "Pen":
        print("\nA heavy fountain pen, with 'v.H' engraved on the cap.")
        print("You press the nib to your thumb...it doesn't leave blue or black ink.")
        print("The ink is crimson red, unsettlingly resembling blood...")

    elif choice == "Book":
        print("\nA nameless book bound in cracked, dark leather.")
        print("You open it on a random page. There is only one sentence written over and over again:")
        print("'The shadow reminds when the light is gone'")

    elif choice == "Newspaper":
        print("\nA scorched clipping from 'El Pais', dated November 1919.")
        print("The headline reads: 'A TRAGIC BLAZE AT AVENIDA DEL TIBIDABO'.")
        print("Most of the article is burnt away, but you can make out:")
        print("'...suspicious circumstances... no remains of the daughter found...")
        print("...police suspect arson...'")

    elif choice == "Vial of Life":
        print("\nA small silver vial filled with a pale, shimmering liquid.")
        print("It feels warm in your palm, as if it remembers a heartbeat.")

    else:
        print(f"\nYou look closely at the {choice}. It seems ordinary enough.")
