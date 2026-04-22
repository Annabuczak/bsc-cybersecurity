import random
import time

time.sleep(3)
import json

inventory = []
items = ["Portal", "The Riddle", "Secret Box"]

rooms = {
    "1": "The Sanctuary",
    "2": "Safe Heaven",
    "3": "The Cursed Estate",
    "4": "House of Eccentrics",
    "5": "The Archive of Unwritten Things",
    "6": "The Place of Torment",
    "7": "The Library of Forgotten Man",

}


def the_sanctuary(inventory):
    while True:
        print("\nSebastian, don't be afraid. The place you dreamed about is real...Welcome to The Sanctuary")
        print("Please look around you, choose one item")
        print("Portal")
        print("The Riddle")
        print("Secret Box")
        choice = input("> ").strip().lower()
        if choice == "Portal":
            print("Leave what you have found here")
        elif choice == "Riddle":
            print("Solve the riddle to find the truth...")
        elif choice == "Secret Box":
            print("When the fragments are restored, the box that once held past, reveles the key to what awaits")
        elif "box" in choice:
            print("You open the box and find The Golden Key")
        elif choice == "Open the door of your choice":
            print("The door opens, and you step into the next chapter of your journey...")
        elif choice == "Stay in The Sanctuary":
            print("Wake up, Sebastian")
            break
        else:
            print("See you in your next dream Sebastian...")


class Inventory:
    def __init__(self, inventory):
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

    def display(self, item):
        if not self.inventory[item]:
            print("Item not found")
        else:
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")

    def get_inventory(self):
        return self.inventory


def print_intro():
    current_room = "The Sanctuary"
    input("Press enter to begin.")
    print(
        "The air smelled of dust and forgotten stories. Somewhere deep inside the labyrinth, a book was waiting…for you...")
    print("Sebastian, wake up from your dream...or reality")
    print("...")
    print("Welcome to the Library of Forgotten Man")
    print(
        "You find yourself in a place that feels both familiar and strange. The air is thick with a sense of nostalgia and mystery")
    print(
        "You are in The Sanctuary, a vast, silent hall where shadow cling to towering shelves filled with books that seem to whisper secrets of the past.")
    print("The scent of old paper and leather fills the air, and the dim light casts eerie shadows on the walls.")
    print(
        "This is where your journey begins, Sebastian. Here, you will uncover the mysteries of the past and confront the forgotten truths about Julian Carax, the broken writer whose soul desires only one thing...revenge.")
    print(
        "Sebastian, to uncover the truth you need to solve the riddle of the Sanctuary.")
    print("Find five items.")
    print("Each item represents identity, love, legacy, creation and tragedy.")
    print("Combined they unlock the box and reveal the Golden Key.")
    print("The Golden Key? Well, don't waste precious time because...")
    print("...it is time to...")
    print("...play the game, Sebastian!")
    print("Good luck and God bless")
    print("...")


print_intro()
