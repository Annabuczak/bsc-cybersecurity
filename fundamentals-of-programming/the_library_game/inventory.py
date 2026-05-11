class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory[item] -= 1
            if self.inventory[item] == 0:
                del self.inventory[item]

    def has_item(self, item_name):
        return item_name in self.inventory.inventory

    def display(self):
        if not self.inventory:
            print("Inventory is empty")
        else:
            for item, qty in self.inventory.items():
                print(f"{item}: {qty}")

    # ⭐ ADD THIS
    def has_item(self, item_name):
        return item_name in self.inventory


def take_item(current_room, rooms, inventory):
    item = rooms[current_room]["item"]

    if item is None:
        print("There is nothing to take here.")
        return

    if item in inventory.inventory:
        print("You already have this item.")
        return

    inventory.add_item(item)
    rooms[current_room]["item"] = None

    print(f"You picked up {item}.")


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


def examine_items(inventory):
    if not inventory.inventory:
        print("\nYour pockets are empty. you have nothing to examine.")
        return

    print("\nYour current inventory:.")
    inventory.display()

    choice = input("Which item do you want to examine? (or type 'none'").strip().title()
    if choice == "none":
        return
    if choice not in inventory.inventory:
        print(f"\nYou don't have {choice}.")
        return

    print(f"\nExamining... {choice}:")

    if choice == "Letter":
        print("""\nThe paper is brittle. The handwriting is hurried, almost desperate.
        "My dearest Penelope...They know. We cannot wait any longer.
        Met me at the Estació de Sants, last train leaves just before midnight.
        If I do not see you, I will assume you changed your mind.
        With undying love. J.C"
        A dark, dried stain covers thr bottom corner.
          """)

    elif choice == "Photo":
        print("""\nIt is the half of torn black-and-white photo.
        Young woman with long, dark hair, smiles at someone out of frame.
        She wears white wedding dress. Her eyes are full of fear""")

    elif choice == "Pen":
        print("""\n A heavy fountain pen, with 'v.H' engraved on the cap.
        You press the nib to your thumb...it doesn't leave blue or black ink.
        The ink is crimson red, unsettlingly resembling blood... """)

    elif choice == "Book":
        print("""\nA nameless blook bound in a cracked, dark leather.
        You open it on a random page. There is only one sentence written over and over again.
        'The shadow remind when the light is gone'
        """)

    elif choice == "Newspaper":
        print("""\nA scorched clipping from 'El Pais', dated November 1919.
        The headlines reads: 'A TRAGIC BLAZE AT AVENIDA DEL TIBIDABO'.
        Most of the article is burnt away, but you can make out a few words: 
        "...suspicious circumstances....no remains of the daughter found...
        ...police suspects arson...
     """)
    else:
        print("""\nYou look closely at the {choice}. It seems ordinary enough""")
