from player import Player, run_game
from inventory import Inventory
from intro_riddle import print_intro
from game_state import game_flags
from save_load import load_game
from rooms import portal_items

while True:
    print("\nWould you like to:")
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")

    choice = input("> ").strip()

    # NEW GAME
    if choice == "1":
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

        print(f"\nWelcome, {player_name}...")

        player = Player(name=player_name)
        player.current_room = "The Sanctuary"
        player.inventory = Inventory()

        run_game(player)

    # LOAD GAME
    elif choice == "2":
        data = load_game()

        if data:
            player = Player(name=data.get("player_name", "Sebastian"))
            player.current_room = data.get("current_room", "The Sanctuary")

            player.inventory = Inventory()
            for item, qty in data.get("inventory", {}).items():
                for _ in range(qty):
                    player.inventory.add_item(item)

            game_flags.update(data.get("game_flags", {}))

            portal_items.clear()
            portal_items.extend(data.get("portal_items", []))

            print(f"\nWelcome back, {player.name}...")

            run_game(player)

        else:
            print("\nNo saved game found.")

    # EXIT
    elif choice == "3":
        print("\nGoodbye!")
        break

    else:
        print("Invalid choice. Try again.")
