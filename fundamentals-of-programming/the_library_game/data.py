# # Attempt to load saved game data from file


data = load_game()
from inventory import Inventory
from movement import move_player
from rooms import rooms

if data:
    # Restore player's last known room
    current_room = data["current_room"]
    # Recreate inventory object (empty first)
    inventory = Inventory()

    # Rebuild inventory items from saved data
    # Saved format: {"item_name": quantity}
    for item, quantity in data["inventory"].items():
        for _ in range(quantity):
            inventory.add_item(item)

# Start new game
else:
    # default starting location
    current_room = "The Sanctuary"

    # Creates empty inventory for new player
    inventory = Inventory()

    # Show available directions from starting room
    for direction, destination in rooms[current_room].items():
        if direction in ["north", "south", "east", "west"]:
            print(f"You can go {direction} to {destination}")
    # Move player based on user input
    current_room = move_player(current_room, rooms)
    # Display current inventory (empty at the start of the game)
    inventory.display()
