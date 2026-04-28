def welome_screen():
    print(
        "The air smelled of dust and forgotten stories. Somewhere deep inside the labyrinth, a book was waiting…for you...")
    print("Sebastian, wake up from your dream...or reality")
    print("...")
    print("Welcome to The Library of Forgotten Man")
    print("Loading. Please wait...")


def menu():
    while True:

        print("Choose one of the following options:")
        print("1. Create a new game")
        print("2. Load a saved game")
        print("3. Exit")

        choice = input("> ").strip()

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

    print_intro()


def print_sleep(param):
    print(param)
    pass
