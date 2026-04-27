from save_load import load_game
from inventory import Inventory
from movement import move_player
from rooms import rooms
from intro_riddle import print_intro

print_intro()

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

while True:
    print(f"\nYou are in {current_room}")

    for direction, destination in rooms[current_room].items():
        if direction != "item":
            print(f"{direction} → {destination}")

    current_room = move_player(current_room, rooms, [])

    inventory.display()
