import json  # Used to convert data to/from JSON format (for saving/loading)

# Used to convert data to/from JSON format (for saving/loading)
SAVE_FILE = "savegame.json"


# Save/Load System Module
# Handles the serialisation and deserialisation of the game state.
# Uses JSON to safely write player progress to a local file and retrieve it,
# allowing for persistent gameplay sessions.
def save_game(player, game_flags, portal_items):
    data = {
        "player_name": player.name,
        "current_room": player.current_room,
        "inventory": player.inventory.inventory,
        "game_flags": game_flags,
        "portal_items": portal_items

    }

    # Open file in writ mode , creates and overwrites file
    with open(SAVE_FILE, "w") as file:
        # Convert dictionary to JSON and save it
        json.dump(data, file, indent=4)

    # Confirnation message
    print("\nGame saved successfully.")


# Attempts to deserialize game state from the local JSON file.
# Uses defensive programming (try/except) to handle cases where
# the player tries to load a game before one exists.
def load_game():
    try:

        with open(SAVE_FILE, "r") as file:

            data = json.load(file)
        # Confirmation message
        print("\nGame loaded successfully.")

        # Return loaded data to main.py
        return data

    except FileNotFoundError:

        print("\nNo saved game found.")

        return None
