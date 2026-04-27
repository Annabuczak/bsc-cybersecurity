def save_game(current_room, inventory):
    with open('savegame.json', 'w') as f:
        json.dump({
            "current_room": current_room,
            "inventory": inventory
        }, f, indent=4)

    saved_data = load_game("savegame.json")

    def load_game(filepath='savegame.json'):
        import os
        import json

        if not os.path.exists(filepath):
            return None

        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return None
