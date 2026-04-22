import random
import time
import json

location = ["The Sanctuary", "Safe Heaven", "The Cursed Estate ", "House of Eccentrics",
            "The Archive of Unwritten Things", "Door with thousands locks"]
inventory = ["Letter", "Wedding photo", "Pen", "Book", "Newspaper"]
items = ["Portal", "The Riddle", "Secret Box"]


def the_sanctuary():
    options = ["Porta", "The Riddle", "Secret Box"]
    while True:
        print("\nSebastian, don't be afraid. The place you dreamed about is real...Welcome to The Sanctuary")
        print("Please look around you, choose one item")
        print("Portal")
        print("The Riddle")
        print("Secret Box")
        choice = input("Enter the name of the item you want to choose: ")
        if choice == "Portal":
            print("Leave what you have found here")
        elif choice == "Riddle":
            print("Solve the riddle to find the truth...")
        elif choice == "Secret Box":
            print("When the fragments are restored, the box that once held past, reveles the key to what awaits")
        elif choice == "Open the door of your choice":
            print("The door opens, and you step into the next chapter of your journey...")
        elif choice == "Stay in The Sanctuary":
            print("Wake up, Sebastian")
            break
        else:
            print("See you in your next dream Sebastian...")


def location(room_list):
    location(room_list)
    print(
        "\n Sebastian, you find yourself in a place that feels both familiar and strange. The air is thick with a sense of nostalgia and mystery. As you look around, you see six doors, each leading to a different location. You can choose to enter any of these doors, but be warned, each one holds its own secrets and challenges.")
    choice = input("Enter the name of the room you want to explore: ")
    if choice == "Safe Heaven":
        print(" Welcome to Sempere and Sons")


def inventory_list(inventory):
    for items in inventory:
        print("1. Letter")
        print("2. Wedding photo")
        print("3. Pen")
        print("4. Book")
        print("5. Newspaper")
