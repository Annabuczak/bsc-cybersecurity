clockwise_order = [

    "Safe Heaven",

    "The Cursed Estate",

    "House of Eccentrics",

    "The Archive of Unwritten Things",

    "The Place of Torment"

]


def move_player(current_room, rooms, clockwise_order):
    print(f"\nYou are in {current_room}")
    print("Which direction would you like to go?")
    for direction in rooms[current_room]:
        print(f"You can go {direction} to {rooms[current_room][direction]}")

    move = input("> ").strip().lower()
    if move not in rooms[current_room]:
        print("You can't go that way.")
        return current_room

    next_room = rooms[current_room][move]

    if current_room == "The Sanctuary":
        if next_room == "Safe Heaven":
            print("You step forward... the journey begins.")
            return next_room
        else:
            print("Something feels wrong... this is not the right path.")
            return current_room

    if current_room in clockwise_order:
        current_index = clockwise_order.index(current_room)

        if current_index + 1 < len(clockwise_order):
            correct_next = clockwise_order[current_index + 1]

            if next_room == correct_next:
                print("You move forward...")
                return next_room
            else:
                print("You feel lost... this is not the correct path.")
                return current_room

    return current_room


def print_map():
    pass
