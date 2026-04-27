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
