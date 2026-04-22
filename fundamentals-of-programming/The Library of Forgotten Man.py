import random
import time
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
        else
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")

    def get_inventory(self):
        return self.inventory
