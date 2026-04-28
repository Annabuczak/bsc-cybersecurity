data = load_game()

if data:
    current_room = data["current_room"]
    inventory = Inventory()

    for item, quantity in data["inventory"].items():
        for _ in range(quantity):
            inventory.add_item(item)
else:
    current_room = "The Sanctuary"
    inventory = Inventory()

    for direction, destination in rooms[current_room].items():
        if direction != "item":
            print(f"You can go {direction} to {destination}")
    current_room = move_player(current_room, rooms, clockwise_order)
    inventory.display()
