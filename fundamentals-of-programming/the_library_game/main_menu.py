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
            saved_data = load_game("savegame.json")
            if saved_data:
                current_room = saved_data["current_room"]
                inventory = saved_data["inventory"]
                print(f"Game Loaded! Current room: {current_room}")
            else:
                print("No saved game found. Starting a new game.")
                current_room = "The Sanctuary"

        elif choice == "3":
            print("Exiting...")
            return "exit"
        else:
            print("Incorrect response. Please try again.")
        print_intro()


def print_sleep(param):
    print(param)
    pass
