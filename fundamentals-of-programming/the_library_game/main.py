from importlib.metadata import pass_none
import os

# Word counter
total_words = 0
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file), "r") as f:
                total_words += len(f.read().split())

print("Total words:", total_words)
from main_menu import menu
from player import Player
from player import run_game
from inventory import Inventory
from intro_riddle import print_intro
from game_state import game_flags
from save_load import load_game
from rooms import portal_items

while True:

    choice = input("\nWould you like to:\n"
                   "1. New Game\n"
                   "2. Load Game\n"
                   "3. Exit\n> ").strip().lower()

    if choice == "1":
        print_intro()

        player = Player()
        player.current_room = "The Sanctuary"
        player.inventory = Inventory()

        run_game(player)


    elif choice == "2":

        data = load_game()

        if data:
            player = Player(name=data["player_name"])
            player.current_room = data["current_room"]

            player.inventory = Inventory()
            for item, qty in data["inventory"].items():
                for _ in range(qty):
                    player.inventory.add_item(item)

            game_flags.update(data.get("game_flags", {}))

            portal_items.clear()
            portal_items.extend(data.get("portal_items", []))

            run_game(player)
        else:
            print("No saved game found.")
    elif choice == "3":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice. Try again.")
