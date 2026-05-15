from save_load import load_game
from inventory import Inventory
from player import Player


def load_or_new_game():
    data = load_game()

    if data:
        # Load existing player
        player = Player(name=data.get("player_name", "Sebastian"))
        player.current_room = data.get("current_room", "The Sanctuary")

        # Restore inventory
        player.inventory = Inventory()
        for item, quantity in data.get("inventory", {}).items():
            for _ in range(quantity):
                player.inventory.add_item(item)

        return player

    else:
        # Start new player
        player = Player()
        return player
