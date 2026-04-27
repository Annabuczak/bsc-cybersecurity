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


def safe_heaven():
    print("You are in Safe Heaven")


def the_cursed_estate():
    print("You are in the Cursed Estate")


def house_of_eccentrics():
    print("You are in the House of Eccentrics")


def the_archive_of_unwritten_things():
    print("You are in the Archives of Unwritten Things")


def the_place_of_torment():
    print("You are in the Place of Torment")


def the_library_of_forgotten_man():
    print("You are in the Library of Forgotten Man")


rooms = {
    "The Sanctuary": {
        "north": "Safe Heaven",
        "east": "House of Eccentrics",
        "item": None
    },

    "Safe Heaven": {
        "south": "The Sanctuary",
        "east": "The Cursed Estate",
        "item": "Letter"
    },

    "The Cursed Estate": {
        "west": "Safe Heaven",
        "north": "The Archive of Unwritten Things",
        "item": "Photo"
    },

    "House of Eccentrics": {
        "west": "The Sanctuary",
        "north": "The Place of Torment",
        "item": "Pen"
    },

    "The Archive of Unwritten Things": {
        "south": "The Cursed Estate",
        "item": "Book"
    },

    "The Place of Torment": {
        "south": "House of Eccentrics",
        "east": "The Library of Forgotten Man",
        "item": "Newspaper"
    },

    "The Library of Forgotten Man": {
        "west": "The Place of Torment",
        "item": None
    }
}
items = ["Portal", "The Riddle", "Secret Box"]
portal_items = []
items_needed = ["Letter", "Photo", "Pen", "Book", "Newspaper"]
