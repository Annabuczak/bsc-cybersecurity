from player import Player, run_game
from inventory import Inventory
from intro_riddle import print_intro
from game_state import game_flags
from save_load import load_game
from rooms import portal_items

while True:
    print("\n1. New Game\n2. Load Game\n3. Exit")
    choice = input("> ")

    if choice == "1":
        print_intro()

        name = input("Your name (or Enter for Sebastian): ").strip()
        if not name:
            name = "Sebastian"

        player = Player(name)
        player.inventory = Inventory()

        game_flags.clear()
        portal_items.clear()

        run_game(player)

    elif choice == "2":
        data = load_game()

        if data:
            player = Player(data.get("player_name", "Sebastian"))
            player.current_room = data.get("current_room", "The Sanctuary")

            player.inventory = Inventory()
            for item, qty in data.get("inventory", {}).items():
                for _ in range(qty):
                    player.inventory.add_item(item)

            game_flags.clear()
            game_flags.update(data.get("game_flags", {}))

            portal_items.clear()
            portal_items.extend(data.get("portal_items", []))

            run_game(player)

        else:
            print("No save found.")

    elif choice == "3":
        print("Goodbye.")
        break
