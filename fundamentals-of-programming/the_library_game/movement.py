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
    print("\nThe map:")
    print(f"You are here: {current_room}")

    rooms_progress = [

        ("Safe Heaven", game_flags.get("safe_heaven_done")),
        ("The Cursed Estate", game_flags.get("estate_done")),
        ("House of Eccentrics", game_flags.get("eccentrics_done")),
        ("Archive", game_flags.get("archive_done")),
        ("Place of Torment", game_flags.get("torment_done")),

    ]

    for room, done in rooms_progress:
        status = "✔" if done else "🔒"

        if room == current_room:
            print(f"➡ {room}")
        else:
            print(f"{status} {room}")


def print_map():
    pass
