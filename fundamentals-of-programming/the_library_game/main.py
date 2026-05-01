import os
from importlib.metadata import pass_none

total_words = 0

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file), "r") as f:
                total_words += len(f.read().split())

print("Total words:", total_words)
from save_load import load_game
from inventory import Inventory
from movement import move_player, clockwise_order
from rooms import rooms
from intro_riddle import print_intro
from main_menu import welome_screen
from main_menu import menu
from sanctuary_menu import sanctuary_menu
from rooms import portal
from intro_riddle import the_riddle
from rooms import secret_box
from NCP import ncp

# MENU
choice = welome_screen()

choice = menu()
if choice == "new_game":
    print_intro()

    current_room = "The Sanctuary"
    inventory = Inventory()

elif choice == "load_game":
    data = load_game()
    if data:
        current_room = data["current_room"]
        inventory = Inventory()
        for item, quantity in data["inventory"].items():
            for _ in range(quantity):
                inventory.add_item(item)
    else:
        print("No saved game found. Starting a new game.")

        current_room = "The Sanctuary"
        inventory = Inventory()
        rooms = rooms()
elif choice == "exit":
    exit()

# GAME LOOP
# GAME LOOP
while True:
    first_time_in_room = True
    if first_time_in_room:
        first_time_in_room = False

    if current_room == "The Sanctuary":
        action = sanctuary_menu()

        if action == "next_room":
            current_room = "Safe Heaven"
            print(f"\nYou are in {current_room}")
            print(rooms[current_room].get("description", ""))
            first_time_in_room = True

        elif action == "Portal":
            portal(inventory)

        elif action == "The Riddle":
            the_riddle()

        elif action == "Secret Box":
            secret_box(inventory)

        elif action == "Door with Thousand Locks":
            print("The door will not budge...")

        elif action == "Enter the only open door":
            print("The door opens, and you step into the next chapter of your journey...")
            print("You are in Safe Heaven")
            current_room = "Safe Heaven"
            print("\nWhat would you like to do?")
            print("1. Talk")
            print("2. Look around")
            print("3. Move")
            print("4. Inventory")

            choice = input(">").strip()

            if choice == "1":
                name = input("Talk to whom? ").lower()

                from NCP import ncp

                room_ncp = ncp.get(current_room, {})

                if name in room_ncp:
                    npc = room_ncp[name]

                    print(npc.get("dialogue", "They say nothing."))
                    print(npc.get("hint", ""))
                else:
                    print("No one by that name is here.")

                continue
            if choice == "2":
                print("Look around discretely")
                continue

            if choice == "3":
                current_room = move_player(current_room, rooms, clockwise_order)

                print(f"\nYou are in {current_room}")
                print(rooms[current_room].get("description", ""))

            if choice == "4":
                inventory.display()
                continue

        elif action == "Exit":
            print("Goodbye,Sebastian")
            exit()
        else:
            break

            # ITEM DISCOVERY
room_data = rooms[current_room]
item = room_data["item"]

current_room = move_player(current_room, rooms, clockwise_order)
room_data = rooms[current_room]
item = room_data["item"]

if item:
    choice = input("Search the roon? y/n? ").strip().lower()

if choice == "y":

    print("Search the room carefully...CHange this ANNa")
    print("You find something hidden ...change this ANNA")

    inventory.add.item(item)

    room_data["item"] = None
else:
    print("you leave the room untouched ...")
