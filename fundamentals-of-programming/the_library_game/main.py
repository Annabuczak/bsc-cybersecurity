items = ["Portal", "The Riddle", "Secret Box"]
portal_items = []
items_needed = ["Letter", "Photo", "Pen", "Book", "Newspaper"]

import os
import time

time.sleep(2)

from save_load import load_game
from intro_riddle import print_intro, the_riddle
from inventory import Inventory
from rooms import the_sanctuary
from rooms import portal
from rooms import secret_box
from save_load import play_again

inventory = Inventory()
the_sanctuary(inventory)
portal(inventory)
secret_box(inventory)

total_words = 0
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file), "r") as f:
                total_words += len(f.read().split())
print("Total words:", total_words)

data = load_game()
if data:
    current_room = data["current_room"]
    inventory = Inventory()
    for item, quantity in data["inventory"].items():
        for _ in range(quantity):
            inventory.add_item(item)
else:
    current_room = "The Sanctuary"
    inventory = Inventory()

data = load_game()

if data:
    current_room = data["current_room"]
    inventory = Inventory()

    for item, quantity in data["inventory"].items():
        for _ in range(quantity):
            inventory.add_item(item)
else:
    current_room = "The Sanctuary"
    inventory = Inventory()

# class colour to be worked on as the code progress#


# SO FAR:
# ROOMS MAP -completed
# CLASS COLOUR - incomplete

# PLAY AGAIN FUNCTION - completed
# PACE FUNCTION - done
# PRINT MAP FUNCTION - to do
# MOVEMENT FUNCTION - DONE
# MENU FUNCTION - DONE
# ROOM FUNCTIONS - in progress
# take FUNCTION - Done
# drop ITEM FUNCTION - TO DO
# use ITEM FUNCTIONS - TO DO


clockwise_order = [

    "Safe Heaven",

    "The Cursed Estate",

    "House of Eccentrics",

    "The Archive of Unwritten Things",

    "The Place of Torment"

]


def menu():
    while True:

        print("\n The Library of Forgotten Man")
        print("Choose one of the following options:")
        print("1. Create a new game")
        print("2. Load a saved game")
        print("3. Exit")
        choice = input("> ").strip()
        print("\nEnter your choice:")
        if choice == "1":
            print("Welcome to The Library of Forgotten Man")
            print("Let's begin the game...")
            return "new_game"
        elif choice == "2":
            saved_data = load_game("savegame.json")
            if saved_data:
                current_room = saved_data["current_room"]
                inventory = saved_data["inventory"]
                print(f"Game Loaded! Current room: {current_room}")
            else:
                print("No saved game found. Starting a new game.")
                current_room = "The Sanctuary"

        elif choice == "3":
            print("Exiting...")
            return "exit"
        else:
            print("Incorrect response. Please try again.")
        print_intro()


def print_sleep(param):
    print(param)

    pass


def print_map():
    pass


def move_player(current_room, rooms, clockwise_order):
    print(f"\nYou are in {current_room}")
    for direction in rooms[current_room]:
        print(f"You can go {direction} to {rooms[current_room][direction]}")

    move = input("> ").strip().lower()
    if move not in rooms[current_room]:
        print("You can't go that way.")
        return current_room

    next_room = rooms[current_room][move]

    if current_room == "The Sanctuary":
        if next_room == "Safe Heaven":
            print("You step forward... the journey begins.")
            return next_room
        else:
            print("Something feels wrong... this is not the right path.")
            return current_room

    if current_room in clockwise_order:
        current_index = clockwise_order.index(current_room)

        if current_index + 1 < len(clockwise_order):
            correct_next = clockwise_order[current_index + 1]

            if next_room == correct_next:
                print("You move forward...")
                return next_room
            else:
                print("You feel lost... this is not the correct path.")
                return current_room

    return current_room


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


def safe_heaven():
    print("You are in Safe Heaven")


def the_cursed_estate():
    print("You are in the Cursed Estate")


def house_of_eccentrics():
    print("You are in the House of Eccentrics")


def the_archive_of_unwritten_things():
    print("You are in the Archives of Unwritten Things")


def the_place_of_torment():
    print("You are in the Place of Torment")


def the_library_of_forgotten_man():
    print("You are in the Library of Forgotten Man")
