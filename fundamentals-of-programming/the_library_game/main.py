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
from inventory import take_item

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

while True:
    print(f"\nYou are in the {current_room} room.")
    print(rooms[current_room].get("description"))
    # THE SANCTUARY LOGIC
    inventory.display()

    choice = welome_screen()

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
        elif action == "Exit":
            print("Goodbye,Sebastian")
            exit()
    # NORMAL ROOM LOGIC
    else:
        print("\nWhat would you like to do?")
        print("1. Talk")
        print("2. Look around")
        print("3. Move")
        print("4. Inventory")

        choice = input(">").strip()

        if choice == "1":
            name = input("Talk to whom? ").lower()
            room_ncp = ncp.get(current_room, {})

            if name in room_ncp:
                npc = room_ncp[name]
                print(f"\nYou aproach{name.lower()}!")

            # NCP MINI LOOP
            while True:
                print(f"\nWhat would you like to do?")
                print("1. Ask for a hint?")
                print("2. Receive an item")
                print("3. Walk away")

                ncp_choice = input(">").lower()

                if ncp_choice == "1":
                    print(f"\nYou aproach{name.lower()}!")
                    print(f"\n{name.lower()}: \"{npc.get('hint', 'I have no advice for you.')}\"")

                elif ncp_choice == "2":
                    print(f"\nYou are being aproached by{name.lower()}!")

                    take_item = input("Do you want to take this item?").lower()
                    if take_item == "yes":
                        inventory.add_item(npc.get("item"))
                        print(f"\nYou received {npc.get('item')} from {name.lower()}!")
                    else:
                        print(f"\nYou declined the item from {name.lower()}.")

                elif ncp_choice == "3":
                    print(f"\nYou step away from {name.lower()}.")
                    break

                else:
                    print("Invalid choice. Please try again.")
        else:
            print("No one by that name is here.")

            room_data = rooms.get(current_room)
            item = room_data.get("item")

            if item:
                search_choice = input("Would you like to search the room? yes/no").lower()
                if search_choice == "yes":
                    print("Search the room...be careful...")
                    print("You find something hidden...")
                    inventory.add_item(item)
                    room_data["item"] = None
                else:
                    print(" You leave the room emptyhanded")
            else:
                print(" You don't seem to find anything")

        if choice == "3":
            current_room = move_player(current_room, rooms, clockwise_order)

            print(f"\nYou are in {current_room}")
            print(rooms[current_room].get("description", ""))

        if choice == "4":
            inventory.display()

        else:
            print("Invalid choice. Choose again.")

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
