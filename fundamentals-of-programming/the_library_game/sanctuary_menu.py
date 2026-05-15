# Handles the interactive numbered menu for the hub .
# Parses numeric user input and returns standardised command strings
# to the main game engine.

def sanctuary_menu():
    # Loop until user selects a valid option
    while True:
        print("Choose from the following options:")
        print("1. Portal")
        print("2. The Riddle")
        print("3. Secret Box ")
        print("4. Door with Thousand Locks")
        print("5. Go to next door")
        print("6. Examine items")
        print("7. Save")
        print("8. Exit")

        # Get user input
        choice = input("> ").strip()

        # Display available actions in The Santuary
        if choice == "1":
            return "Portal"  # Display portal
        elif choice == "2":
            return "The Riddle"  # View The Riddle
        elif choice == "3":
            return "Secret Box"  # Attempts to open The Secret Box
        elif choice == "4":
            return "Door with Thousand Locks"  # Final Door
        elif choice == "5":
            return "Enter the only open door"  # Move to next door
        elif choice == "6":
            return "Examine items"  # Inspect inventory
        elif choice == "7":
            return "Save"  # Save game
        elif choice == "8":  # Exit game
            return "Exit"
        else:
            print("Invalid choice. Please choose a number from 1 to 8.")
