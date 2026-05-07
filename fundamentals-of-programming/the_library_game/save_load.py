import json
import os
import time

time.sleep(2)

SAVE_FILE = "savegame.json"


def save_game(player, game_flags, portal_items):
    data = {
        "player_name": player.name,
        "current_room": player.current_room,
        "inventory": player.inventory.inventory,
        "game_flags": game_flags,
        "portal_items": portal_items

    }

    with open(SAVE_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("\nGame saved successfully.")


def load_game():
    try:

        with open(SAVE_FILE, "r") as file:

            data = json.load(file)

        print("\nGame loaded successfully.")

        return data

    except FileNotFoundError:

        print("\nNo saved game found.")

        return None
