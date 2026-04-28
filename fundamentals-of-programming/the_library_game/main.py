from save_load import load_game
from inventory import Inventory
from movement import move_player, clockwise_order
from rooms import rooms
from intro_riddle import print_intro
from main_menu import welome_screen
from main_menu import menu
from sanctuary_menu import sanctuary_menu

# MENU
choice = welome_screen()

choice = menu()
if choice == "new_game":

    current_room = "The Sanctuary"
    inventory = Inventory()

elif choice == "load_game":
    data = load_game()
    if data:
        current_room = data["current_room"]
        inventory = Inventory()
        for item, quantity in data["inventory"].items():
            for _ in range(quantity):
                inventory.add_item(item)
    else:
        print("No saved game found. Starting a new game.")

        current_room = "The Sanctuary"
        inventory = Inventory()
        rooms = rooms()
elif choice == "exit":
    exit()

# GAME LOOP
# GAME LOOP
while True:
    print(f"\nYou are in {current_room}")  # ✅ ALWAYS show room

    inventory.display()
    if current_room == "The Sanctuary":
        action = sanctuary_menu()

        if action == "next_room":
            current_room = "Safe Heaven"

        elif action == "Portal":
            print("The portal hums quietly...")

        elif action == "The Riddle":
            print("You recall the riddle...")

        elif action == "Secret Box":
            print("The box is locked...")

        elif action == "Door with Thousand Locks":
            print("The door will not budge...")

        elif action == "Enter the only open door":
            print("The door opens, and you step into the next chapter of your journey...")

        elif action == "Exit":
            exit()
        else:
            current_room = move_player(current_room, rooms, clockwise_order)
