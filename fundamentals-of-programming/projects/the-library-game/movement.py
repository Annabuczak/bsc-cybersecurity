# Movement & Navigation Module
# Handles the spatial logic of the labyrinth.
# Parses directional inputs against the room dictionary to allow movement,
# and renders an ASCII map to help the player visualize their location.


# Parses the current room's available exits and prompts the player for movement.
# Prevents invalid directional commands and updates the player's location.
def move_player(current_room, rooms):
    valid_directions = ["north", "south", "east", "west"]

    # Build dictionary of available moves from current room
    available_moves = {}
    for key, value in rooms[current_room].items():
        if key in valid_directions:
            available_moves[key] = value

    # No exits available
    if not available_moves:
        print("\nThere are no visible doors or paths from here.")
        return current_room

    # Show available paths 
    print("\nAvailable paths:")
    for direction, next_room in available_moves.items():
        print(f"- Go {direction} to {next_room}")

    # Ask player for input
    move = input("\nWhich direction would you like to go? (or type 'cancel')\n> ").strip().lower()

    # Cancel movement
    if move == 'cancel':
        print("\nYou decide to stay where you are.")
        return current_room
    # Valid move
    elif move in available_moves:
        print(f"\nYou walk {move} into the shadows...")
        return available_moves[move]

    # Invlid direction
    else:
        print("\nYou can't go that way. Please type a valid direction (e.g., 'north', 'south').")
        return current_room


# Display simple vertical map layout
def show_map(current_room, game_flags):
    print("\n" + "=" * 35)
    print("           THE MAP")
    print("=" * 35 + "\n")

    # Helper function to format room display
    def mark(room_name):

        # Highlight current room
        if room_name == current_room:
            return f"[{room_name.upper()}]"


        elif not game_flags.get(room_name.lower().replace(" ", "_") + "_done", False):
            return "[???]"

        # Visited room
        else:
            return f"[{room_name}]"

        # Redrawn to exactly match the North/South/East/West layout of rooms.py

    print(f"                                   {mark('The Library of Forgotten Man')}")
    print("                                            |")
    print(f"             {mark('The Place of Torment')} ----------+ (East)")
    print("                       | (North)")
    print(f"      {mark('The Archive of Unwritten Things')}")
    print("                       | (North)")
    print(f"             {mark('House of Eccentrics')}")
    print("                       | (North)")
    print(f"             {mark('The Cursed Estate')}")
    print("                       |")
    print(f" {mark('Safe Heaven')} ---------+ (East)")
    print("      | (North)")
    print(f" {mark('The Sanctuary')}")

    # Hidden chamber hint
    if game_flags.get("hidden_unlocked"):
        print("\n        ??? → [Forgotten Chamber]")
