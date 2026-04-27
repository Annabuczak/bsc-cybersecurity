import json
import os


def save_game(current_room, inventory):
    with open('savegame.json', 'w') as f:
        json.dump({
            "current_room": current_room,
            "inventory": inventory
        }, f, indent=4)


def load_game(filepath='savegame.json'):
    if not os.path.exists(filepath):
        return None

    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None
