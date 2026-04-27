import json
import os
import time

time.sleep(2)


def save_game(current_room, inventory):
    with open('savegame.json', 'w') as f:
        json.dump({
            "current_room": current_room,
            "inventory": inventory
        }, f, indent=4)


def load_game(filepath='savegame.json'):
    if not os.path.exists(filepath):
        return None

    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def play_again():
    while True:
        again = input("\nWould you like to play again? (yyes/no)").strip().lower()
        if again == 'no':
            print_sleep("Thanks for playing! See you next time.")
            exit()
        elif again == 'yes':
            menu()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
