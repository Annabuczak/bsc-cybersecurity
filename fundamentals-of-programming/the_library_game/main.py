import os
import time
import sys
import json

import textwrap

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
from main_menu import menu
from sanctuary_menu import sanctuary_menu
from rooms import portal
from intro_riddle import the_riddle
from rooms import secret_box
from NCP import ncp
from deadlybookpuzzle import deadlybookpuzzle
from cursed_estate import explore_estate
from inventory import take_item
from inventory import examine_items
from Blood_contract import blood_contract_puzzle
from blank_book import blank_book_puzzle
from Iron_door import iron_door_puzzle
from game_state import handle_mistake, game_flags
from game_formatting import divider, slow_print, print_description
from player import Player

# MENU
choice = menu()
if choice == "new_game":
    print_intro()
    print("\nBefore we begin...")
    print("1. Enter your name")
    print("2. Continue as Sebastian")

    name_choice = input("> ").strip()
    if name_choice == "1":
        player_name = input("\nWhat is your name? ").strip()
        if not player_name:
            player_name = "Sebastian"

    else:
        player_name = "Sebastian"
    print(f"\nWelcome, {player_name}!")

    player = Player(name=player_name)

    current_room = "The Sanctuary"
    player = Player()

elif choice == "load_game":
    data = load_game()
    if data:
        player = Player()
        player.current_room = data["current_room"]
        player.inventory = Inventory()
        for item, quantity in data["inventory"].items():
            for _ in range(quantity):
                player.inventory.add_item(item)
    else:
        print("No saved game found. Starting a new game.")
        player = Player()
        current_room = "The Sanctuary"
        player.inventory = Inventory()
        rooms = rooms()
elif choice == "exit":
    exit()

# GAME LOOP
while True:
    print(f"\nYou are in the {player.current_room} room.")
    print(rooms[player.current_room].get("description", ""))

    # THE SANCTUARY LOGIC
    if player.current_room == "The Sanctuary":
        player.inventory.display()

        action = sanctuary_menu()

        if action == "next_room":
            player.current_room = "Safe Heaven"
            print(f"\nYou are in {player.current_room}")
            print(rooms[player.current_room].get("description", ""))
            first_time_in_room = True
            handle_mistake()

        elif action == "Portal":
            portal(player.inventory)
            handle_mistake()

        elif action == "The Riddle":
            the_riddle()

        elif action == "Secret Box":
            secret_box(player.inventory)
            handle_mistake()
        elif action == "Door with Thousand Locks":
            print("The door will not budge...")
            handle_mistake()

        elif action == "Enter the only open door":
            if rooms.get("Safe Heaven", {}).get("item") is None:
                player.current_room = "The Cursed Estate"
                print("\nThe door to Safe Heaven has sealed shut.")
                print("A darker path opens before you...")
                print(f"\nYou are in {player.current_room}")
                print(rooms[player.current_room].get("description", ""))

            else:
                current_room = "Safe Heaven"
                print("\nThe door opens, and you step into the antiquarian bookshop...")
                print(f"\nYou are in {player.current_room}")
                print(rooms[player.current_room].get("description", ""))

        elif action == "Exit":
            print("Goodbye, Sebastian")
            exit()

    # NORMAL ROOM LOGIC
    else:
        print("\nWhat would you like to do?")
        print("People here:", ", ".join(ncp.get(player.current_room, {}).keys()) or "No one.")
        print("1. Talk")
        print("2. Look around")
        print("3. Move")
        print("4. Inventory")
        print("5. Go back to The Sanctuary")
        print("6. Examin an item")

        choice = input(">").strip()

        if choice == "1":
            name = input("Approach whom? ").lower().strip()
            room_ncp = ncp.get(player.current_room, {})

            if name in room_ncp:
                chosen_ncp = room_ncp[name]
                print(f"\nYou approach {name.lower()}!")

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
                        print(f"\n{name.lower()}: \"{chosen_ncp.get('dialogue', '...')}\"")

                    elif ncp_choice == "2":
                        print(f"\n{name.lower()}: \"{chosen_ncp.get('hint', 'I have no advice for you.')}\"")

                    elif ncp_choice == "3":
                        item_to_give = chosen_ncp.get("gives")
                        if item_to_give and item_to_give != "None":
                            take_item = input(f"Do you want to take the {item_to_give}? (yes/no): ").strip().lower()
                            if take_item == "yes":
                                player.inventory.add_item(item_to_give)
                                print(f"\nYou received {item_to_give} from {name.lower()}!")
                                chosen_ncp["gives"] = None  # Removes the item so they can't give it twice!
                            else:
                                print(f"\nYou declined the item from {name.capitalize()}.")
                        else:
                            print(f"\n{name.lower()} has nothing to give you right now.")

                    elif ncp_choice == "4":
                        print(f"\nYou step away from {name.lower()}.")
                        break

                    elif ncp_choice == "5":
                        print(f"\nReturning to The Sanctuary.")
                        player.current_room = "The Sanctuary"
                        break

                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("No one by that name is here.")

        elif choice == "2":
            print("\nYou look around discreetly...")
            room_data = rooms.get(player.current_room, {})
            item = room_data.get("item")

            # THE DEADLY BOOK PUZZLE (SAFE HEAVEN ONLY)
            if player.current_room == "Safe Heaven" and item:
                deadlybookpuzzle(player.inventory, player.current_room, rooms)

            # THE CURSED ESTATE PUZZLE
            elif player.current_room == "The Cursed Estate" and item:
                explore_estate(player.inventory, rooms[player.current_room])

            # THE BLOOD COTRACT PUZZLE
            elif player.current_room == "House of Eccentrics" and item:
                success = blood_contract_puzzle(player.inventory)
                if success:
                    rooms[player.current_room]["item"] = None


            # THE BLANK BOOK PUZZLE
            elif player.current_room == "The Archive of Unwritten Things" and item:
                success = blank_book_puzzle(player.inventory)
                if success:
                    rooms[player.current_room]["item"] = None

            # IRON DOOR PUZZLE
            elif player.current_room == "The Place of Torment":
                success = iron_door_puzzle(player.inventory)
                if success:
                    rooms[player.current_room]["item"] = None

            elif item:
                search_choice = input("Would you like to search the room? (yes/no): ").strip().lower()
                if search_choice == "yes":
                    print("Searching the room... be careful...")
                    print(f"You find something hidden: {item}")
                    player.inventory.add_item(item)
                    rooms[player.current_room]["item"] = None
                else:
                    print("You leave the room empty-handed.")
            else:
                print("You don't seem to find anything.")

        elif choice == "3":
            player.current_room = move_player(player.current_room, rooms)

        elif choice == "4":
            player.inventory.display()

        elif choice == "5":
            print("\nReturning to The Sanctuary.")
            player.current_room = "The Sanctuary"
        elif choice == "6":
            examine_items(player.inventory)

        else:
            print("Invalid choice. Choose again.")
