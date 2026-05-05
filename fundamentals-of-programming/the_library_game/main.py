import os
from importlib.metadata import pass_none

# Word counter
total_words = 0
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file), "r") as f:
                total_words += len(f.read().split())

print("Total words:", total_words)

# Imports
from save_load import load_game
from inventory import Inventory
from movement import move_player
from rooms import rooms
from intro_riddle import print_intro
from main_menu import welome_screen
from main_menu import menu
from sanctuary_menu import sanctuary_menu
from rooms import portal
from intro_riddle import the_riddle
from rooms import secret_box
from NCP import ncp
from deadlybookpuzzle import deadlybookpuzzle
from cursed_estate import explore_estate
from inventory import take_item

# MENU
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
    print(rooms[current_room].get("description", ""))

    # THE SANCTUARY LOGIC
    if current_room == "The Sanctuary":
        inventory.display()
       
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
            if rooms.get("Safe Heaven", {}).get("item") is None:
                current_room = "The Cursed Estate"
                print("\nThe door to Safe Heaven has sealed shut.")
                print("A darker path opens before you...")
                print(f"\nYou are in {current_room}")
                print(rooms[current_room].get("description", ""))
            else:
                current_room = "Safe Heaven"
                print("\nThe door opens, and you step into the antiquarian bookshop...")
                print(f"\nYou are in {current_room}")
                print(rooms[current_room].get("description", ""))

        elif action == "Exit":
            print("Goodbye, Sebastian")
            exit()

    # NORMAL ROOM LOGIC
    else:
        print("\nWhat would you like to do?")
        print("People here:", ", ".join(ncp.get(current_room, {}).keys()) or "No one.")
        print("1. Talk")
        print("2. Look around")
        print("3. Move")
        print("4. Inventory")
        print("5. Go back to The Sanctuary")

        choice = input(">").strip()

        if choice == "1":
            name = input("Approach whom? ").lower().strip()
            room_ncp = ncp.get(current_room, {})

            if name in room_ncp:
                chosen_ncp = room_ncp[name]
                print(f"\nYou approach {name.capitalize()}!")

                # NCP MINI LOOP
                while True:
                    print(f"\nWhat would you like to do with {name.capitalize()}?")
                    print("1. Talk")
                    print("2. Ask for a hint")
                    print("3. Find an item")
                    print("4. Walk away")
                    print("5. Return to The Sanctuary")

                    ncp_choice = input(">").strip()

                    if ncp_choice == "1":
                        print(f"\n{name.capitalize()}: \"{chosen_ncp.get('dialogue', '...')}\"")

                    elif ncp_choice == "2":
                        print(f"\n{name.capitalize()}: \"{chosen_ncp.get('hint', 'I have no advice for you.')}\"")

                    elif ncp_choice == "3":
                        item_to_give = chosen_ncp.get("gives")
                        if item_to_give and item_to_give != "None":
                            take_item = input(f"Do you want to take the {item_to_give}? (yes/no): ").strip().lower()
                            if take_item == "yes":
                                inventory.add_item(item_to_give)
                                print(f"\nYou received {item_to_give} from {name.capitalize()}!")
                                chosen_ncp["gives"] = None  # Removes the item so they can't give it twice!
                            else:
                                print(f"\nYou declined the item from {name.capitalize()}.")
                        else:
                            print(f"\n{name.capitalize()} has nothing to give you right now.")

                    elif ncp_choice == "4":
                        print(f"\nYou step away from {name.capitalize()}.")
                        break

                    elif ncp_choice == "5":
                        print(f"\nReturning to The Sanctuary.")
                        current_room = "The Sanctuary"
                        break

                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("No one by that name is here.")

        elif choice == "2":
            print("\nYou look around discreetly...")
            room_data = rooms.get(current_room, {})
            item = room_data.get("item")

            # THE DEADLY BOOK PUZZLE (SAFE HEAVEN ONLY)
            if current_room == "Safe Heaven" and item:
                deadlybookpuzzle(inventory, current_room, rooms)

            # THE CURSED ESTATE PUZZLE
            elif current_room == "The Cursed Estate" and item:
                explore_estate(inventory, rooms[current_room])

            elif item:
                search_choice = input("Would you like to search the room? (yes/no): ").strip().lower()
                if search_choice == "yes":
                    print("Searching the room... be careful...")
                    print(f"You find something hidden: {item}")
                    inventory.add_item(item)
                    rooms[current_room]["item"] = None
                else:
                    print("You leave the room empty-handed.")
            else:
                print("You don't seem to find anything.")

        elif choice == "3":
            current_room = move_player(current_room, rooms)

        elif choice == "4":
            inventory.display()

        elif choice == "5":
            print("\nReturning to The Sanctuary.")
            current_room = "The Sanctuary"

        else:
            print("Invalid choice. Choose again.")
