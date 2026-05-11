# Main Menu
# Control the entry point of application
# Handles player creation, loading saved states, and exiting the game.

# Import
from player import Player, run_game
from inventory import Inventory
from intro_riddle import print_intro
from game_state import game_flags
from save_load import load_game
from rooms import portal_items

# Displays main menu options
while True:
    print("1. New game")
    print("2. Save")
    print("3. Exit")

    # Get user input
    choice = input("> ")
    # New game
    if choice == "1":
        print_intro()  # Print introduction to the game

        # Player is ask for their name
        name = input("Your name (or Enter for Sebastian): ").strip()
        if not name:  # choice of generic name "Sebastian"
            name = "Sebastian"

        # welcome message
        print(f"\nWelcome, {name}...")

        # Creates new player object
        player = Player(name)
        # Initial inventory
        player.inventory = Inventory()

        # Reset all game progress flags
        game_flags.clear()
        # Reset items placed in the portal
        portal_items.clear()

        # Starts main game loop
        run_game(player)
    # Load game
    elif choice == "2":
        # Loads saved data
        data = load_game()

        # If saved data exists
        if data:
            # Restores players name
            player = Player(data.get("player_name", "Sebastian"))

            # Restores current room
            player.current_room = data.get("current_room", "The Sanctuary")

            # Rebuild inventory from saved
            player.inventory = Inventory()
            for item, qty in data.get("inventory", {}).items():
                for _ in range(qty):
                    player.inventory.add_item(item)

            # Restores game flags (progress, unlocks)
            game_flags.clear()
            game_flags.update(data.get("game_flags", {}))

            # Restore portal items (used for secret box,)
            portal_items.clear()
            portal_items.extend(data.get("portal_items", []))

            # Resume game
            run_game(player)

        else:
            # No save found
            print("No save found.")

    # exit the game
    elif choice == "3":
        print("Goodbye.")
        break  # Exit main loop safely
