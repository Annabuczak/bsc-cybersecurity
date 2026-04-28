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


rooms = rooms = {
    "The Sanctuary": {
        "north": "Safe Heaven",
        "item": None,

    },

    "Safe Heaven": {
        "south": "The Sanctuary",
        "east": "The Cursed Estate",
        "item": "Letter"
                "description" "A place of solace and safety,"
                " where the air is filled with a sense of calm and tranquility."
                " The walls are adorned with soft, warm colors, and the atmosphere is serene. "
                "It's a haven from the outside world, offering comfort and refuge to those who seek it."
    },

    "The Cursed Estate": {
        "west": "Safe Heaven",
        "north": "House of Eccentrics",
        "item": "Photo"
    },

    "House of Eccentrics": {
        "south": "The Cursed Estate",
        "north": "The Archive of Unwritten Things",
        "item": "Pen"
    },

    "The Archive of Unwritten Things": {
        "south": "House of Eccentrics",
        "north": "The Place of Torment",
        "item": "Book"
    },

    "The Place of Torment": {
        "south": "The Archive of Unwritten Things",
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
