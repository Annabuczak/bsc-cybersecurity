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
from main_menu import menu
from main_menu import print_sleep
from movement import move_player
from movement import print_map
from inventory import take_item
from inventory import drop_item
from rooms import safe_heaven
from rooms import the_cursed_estate
from rooms import house_of_eccentrics
from rooms import the_archive_of_unwritten_things
from rooms import the_place_of_torment
from rooms import the_library_of_frogtten_man

inventory = Inventory()
the_sanctuary(inventory)
portal(inventory)
secret_box(inventory)
print_intro()
move_player()
menu()
play_again()
print_sleep()
print_map()
take_item(inventory)
drop_item(inventory)
room = safe_heaven
rooms = the_cursed_estate
rooms = the_place_of_torment
rooms = the_archive_of_unwritten_things
rooms = house_of_eccentrics
rooms = the_library_of_frogtten_man

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

for direction in rooms[current_room]:
    if direction != "item":
        print(f"You can go {direction} to {rooms[current_room][direction]}")

# CLASS COLOUR - incomplete
# drop ITEM FUNCTION - TO DO
# use ITEM FUNCTIONS - TO DO
