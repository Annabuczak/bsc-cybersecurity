def move_player(current_room, rooms):
    valid_directions = ["north", "south", "east", "west"]

    available_moves = {}
    for key, value in rooms[current_room].items():
        if key in valid_directions:
            available_moves[key] = value

    if not available_moves:
        print("\nThere are no visible doors or paths from here.")
        return current_room

    print("\nAvailable paths:")
    for direction, next_room in available_moves.items():
        print(f"- Go {direction} to {next_room}")

    move = input("\nWhich direction would you like to go? (or type 'cancel')\n> ").strip().lower()

    if move == 'cancel':
        print("\nYou decide to stay where you are.")
        return current_room

    elif move in available_moves:
        print(f"\nYou walk {move} into the shadows...")
        return available_moves[move]

    else:
        print("\nYou can't go that way. Please type a valid direction (e.g., 'north', 'south').")
        return current_room


def show_map(current_room, game_flags):
    print("\n" + "=" * 35)
    print("           THE MAP")
    print("=" * 35 + "\n")

    def mark(room_name):

        if room_name == current_room:
            return f"[{room_name.upper()}]"

        elif not game_flags.get(room_name.lower().replace(" ", "_") + "_done", False):
            return f"[{room_name}]"

        else:
            return f"[{room_name}]"

    print(f"        {mark('The Place of Torment')}")
    print("                 |")

    print(f" {mark('The Archive of Unwritten Things')} — {mark('House of Eccentrics')}")
    print("                 |")

    print(f"        {mark('The Cursed Estate')}")
    print("                 |")

    print(f"        {mark('Safe Heaven')}")
    print("                 |")

    print(f"        {mark('The Sanctuary')}")

    if game_flags.get("hidden_unlocked"):
        print("\n        ??? → [Forgotten Chamber]")
