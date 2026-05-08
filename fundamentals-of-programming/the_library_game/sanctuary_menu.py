def sanctuary_menu():
    while True:
        print("Choose from the following options:")
        print("1. Portal")
        print("2. The Riddle")
        print("3. Secret Box ")
        print("4. Door with Thousand Locks")
        print("5. Go to next door")
        print("6. Examine items")
        print("7. Exit")
        choice = input("> ").strip()
        if choice == "1":
            return "Portal"
        elif choice == "2":
            return "The Riddle"
        elif choice == "3":
            return "Secret Box"
        elif choice == "4":
            return "Door with Thousand Locks"
        elif choice == "5":
            return "Enter the only open door"
        elif choice == "6":
            return "Examine items"
        elif choice == "7":
            return "Save"
        elif choice == "8":
            return "Exit"
