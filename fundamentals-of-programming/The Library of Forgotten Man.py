with open("The Library of Forgotten Man.py", "r") as f:
    text = f.read()

    print(len(text.split()))
# SO FAR:
# ROOMS -completed
# SANCTUARY INVENTORY - completed
# CLASS COLOUR - incomplete
# CLASS INVENTORY - completed
# PRINT INTRO TO THE GAME - done
# THE RIDDLE - completed
# PORTAL FUNCTION - completed
# SECRET BOX FUNCTION - done
# PLAY AGAIN FUNCTION - completed
# PACE FUNCTION - done
# PRINT MAP FUNCTION - to do
# MOVEMENT FUNCTION - DONE
# MAIN FUNCTION - IN PROGRESS


# DEF ORDER ( TO BE SORTED)


import random
import time

time.sleep(2)
import json

items = ["Portal", "The Riddle", "Secret Box"]

# player has everything
rooms = {
    "1": "The Sanctuary",
    "2": "Safe Heaven",
    "3": "The Cursed Estate",
    "4": "House of Eccentrics",
    "5": "The Archive of Unwritten Things",
    "6": "The Place of Torment",
    "7": "The Library of Forgotten Man",

}


def menu():
    while True:

        print("\n The Library of Forgotten Man")
        print("Choose one of the following options:")
        print("1. Create a new game")
        print("2. Load a saved game")
        print("3. Exit")
        choice = input("> ").strip()
        print("\nEnter your choice:")
        if choice == "1":
            print("Welcome to The Library of Forgotten Man")
            print("Let's begin the game...")
            return "new_game"
        elif choice == "2":
            print("Loading saved game...")
            return "load_game"
        elif choice == "3":
            print("Exiting...")
            return "exit"
        else:
            print("Incorrect response. Please try again.")


def the_sanctuary(inventory):
    while True:
        print("\nSebastian, don't be afraid. The place you dreamed about is real...Welcome to The Sanctuary")
        print("Please look around you, choose one item")
        print("Portal")
        print("The Riddle")
        print("Secret Box")
        choice = input("> ").strip().lower()
        if choice == "portal":
            print("Leave what you have found here")
        elif choice == "riddle":
            print("Solve the riddle to find the truth...")
            the_riddle()
        elif choice == "secret box":
            print("When the fragments are restored, the box that once held past, reveles the key to what awaits")
        elif "box" in choice:
            print("You open the box and find The Golden Key")
        elif choice == "Open the door of your choice":
            print("The door opens, and you step into the next chapter of your journey...")
        elif choice == "Stay in The Sanctuary":
            print("Wake up, Sebastian")
            break
        else:
            print("See you in your next dream Sebastian...")


# class colour to be worked on as the code progress#
class Colours:
    REDtext = '\033[91m'
    GREENtext = '\033[92m'
    YELLOWtext = '\033[93m'
    BLUEtext = '\033[94m'
    MAGENTAtext = '\033[95m'
    CYANtext = '\033[96m'
    WHITEtext = '\033[97m'
    RESETtext = '\033[0m'
    NORMALWHITEtext = '\033[0m'
    BOLDtext = '\033[1m'


def print_WHITEtext(text):
    print(Colours.WHITEtext + text + Colours.RESETtext)


def printNarrationText(message=None):
    if message is None:
        message = []

    for msg in message:
        print(Colours.blueText + msg + Colours.RESETtext)


class Inventory:
    def __init__(self, inventory):
        self.inventory = {}

    def add_item(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1
        print(self.inventory)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory[item] -= 1
            if self.inventory[item] == 0:
                del self.inventory[item]
        else:
            print("Item not found")

    def display(self, item):
        if not self.inventory:
            print("Inventory is empty")
        else:
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")

    def get_inventory(self):
        return self.inventory


def print_intro():
    current_room = "The Sanctuary"
    print(
        "The air smelled of dust and forgotten stories. Somewhere deep inside the labyrinth, a book was waiting…for you...")
    print("Sebastian, wake up from your dream...or reality")
    print("...")
    print("Welcome to the Library of Forgotten Man")
    print(
        "You find yourself in a place that feels both familiar and strange. The air is thick with a sense of nostalgia and mystery")
    print(
        "You are in The Sanctuary, a vast, silent hall where shadow cling to towering shelves filled with books that seem to whisper secrets of the past.")
    print("The scent of old paper and leather fills the air, and the dim light casts eerie shadows on the walls.")
    print(
        "This is where your journey begins, Sebastian. Here, you will uncover the mysteries of the past and confront the forgotten truths about Julian Carax, the broken writer whose soul desires only one thing...revenge.")
    print(
        "Sebastian, to uncover the truth you need to solve the riddle of the Sanctuary.")
    print("Find five items.")
    print("Each item represents identity, love, legacy, creation and tragedy.")
    print("Combined they unlock the box and reveal the Golden Key.")
    print("The Golden Key? Well, don't waste precious time because...")
    print("...it is time to...")
    print("...play the game, Sebastian!")
    print("Good luck and God bless")
    print("...")


print_intro()


def the_riddle():
    current_room = "The Sanctuary"
    print("Solve the riddle to find the truth...")
    print("...")
    print("Five fragments lie where shadows keep,")
    print("In silent ink and memories deep.")
    print("...")
    print("Begin where silence shelters truth")
    print(" Where quiet souls are laid to rest")
    print("...")
    print("A name concealed in crimson thread,")
    print("A love remembered, through half is dead.")
    print("...")
    print("Seek next the halls where sorrow stays,")
    print("A house still bound to darker days.")
    print("...")
    print("Then walk where echoes twist the mind")
    print("Where curious thoughts grow unconfines")
    print("Where histories are written in sacred black blood")
    print("...")
    print("Beyond, where words were never penned,")
    print("The truths unfinished start to bend.")
    print("...")
    print("A story lost, yet still your own,")
    print("A truth consumed by ash and flame")
    print("...")
    print("Restore the past to reclaim the name")


def portal(inventory):
    required_items = ["Letter", "Photo", "Pen", "Book", "Newspaper"]

    if all(item in inventory.inventory for item in required_items):
        print("You have entered the portal!")
    else:
        print("I'm afraid you can't go any further, Sebastian.")
        return

    while True:
        print("welcome back...")

        choice = input("Would you like to open the box and find the truth? (yes/no) ").strip().lower()

        if choice == "yes":
            print("open the box and find the truth...")

        elif choice == "no":
            print("You are not ready to face the truth, Sebastian. The Game ends here for you. Farewell.")
            break

        elif choice == "x":
            break

        else:
            print("Invalid choice.")


def secret_box(inventory):
    required_items = ["Letter", "Photo", "Pen", "Book", "Newspaper"]

    if all(item in inventory.inventory for item in required_items):
        print("When the fragments are restored...")
        print("Open the box and find The Golden Key")
    else:
        print("You are not ready to face the truth, Sebastian.")


def print_sleep(param):
    print(param)
    time.sleep(1)
    pass


def play_again():
    while True:
        again = input("\nWould you like to play again? (yyes/no)").strip().lower()
        if again == 'no':
            print_sleep("Thanks for playing! See you next time.")
            exit()
        elif again == 'yes':
            main()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def print_map():
    pass


def movment():
    while True:
        print_map()
        print("\n Which direction would you like to go?")
        print("1. North")
        print("2. East")
        print("3. South")
        print("4. West")
        print("5. Go to main menu")
        move = input(" > ").strip()
        if move == '1':
            x, y = (-1, 0)
        elif move == '2':
            x, y = (0, 1)
        elif move == '3':
            x, y = (1, 0)
        elif move == '4':
            x, y = (0, -1)
        elif move == '5':
            break
        else:
            print("Invalid input. Please enter correct number")
            continue
        print(f"Moving to direction: {x}, {y}")
