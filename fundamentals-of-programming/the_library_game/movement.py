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


def show_map(current_room, flags):
    print("\nYou are here:{current_room}")

    rooms_progress = [
        ("Safe Heaven", flags.get("safe_heaven_done")),
        ("The Cursed Estate", flags.get("cursed_estate_done")),
        ("House of Eccentrics", flags.get("houseof_estate_done")),
        ("The Archive of Unwritten Things", flags.get("archive_of_things_done")),
        ("The Place of Torment", flags.get("place_of_torment_done")),
        ("The Library of Forgotten Man", flags.get("library_of_forgotten_man_done")),
    ]
    print("Progress\\\n")
    for room, done in rooms_progress:
        status = "*tick* if done else """
        print("f[{status}], [{room}]")
        

def print_map():
    pass
