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

    def mark(room_name, current_room, game_flags):

        if room_name == current_room:

            return f"[{room_name.upper()}]"

        elif not game_flags.get(room_name.lower().replace(" ", "_") + "_done", True):

            return "[LOCKED]"

        else:

            return f"[{room_name}]"

    print(f"        {mark('The Place of Torment', current_room, game_flags)}")
    print("                 |")

    print(
        f" {mark('The Archive of Unwritten Things', current_room, game_flags)} — {mark('House of Eccentrics', current_room, game_flags)}")
    print("                 |")

    print(f"        {mark('The Cursed Estate', current_room, game_flags)}")
    print("                 |")

    print(f"        {mark('Safe Heaven', current_room, game_flags)}")
    print("                 |")

    print(f"        {mark('The Sanctuary', current_room, game_flags)}")

    rooms_progress = [

        ("Safe Heaven", game_flags.get("safe_heaven_done")),
        ("The Cursed Estate", game_flags.get("estate_done")),
        ("House of Eccentrics", game_flags.get("eccentrics_done")),
        ("The Archive of Unwritten Things", game_flags.get("archive_done")),
        ("Place of Torment", game_flags.get("torment_done")),

    ]

    for room, done in rooms_progress:
        status = "✔" if done else "🔒"

        if room == current_room:
            print(f"➡ {room}")
        else:
            print(f"{status} {room}")

    completed = sum([
        game_flags.get("safe_heaven_done", False),
        game_flags.get("estate_done", False),
        game_flags.get("eccentrics_done", False),
        game_flags.get("archive_done", False),
        game_flags.get("torment_done", False),
    ])

    total = 5

    percent = int((completed / total) * 100)

    print(f"\nProgress: {percent}% complete")
