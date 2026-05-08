from game_state import handle_mistake


def iron_door_puzzle(inventory):
    print("\nThe iron door stands before you.")
    print("A mechanical lock waits for a 4-digit code.")

    guess = input("\nEnter the 4-digit code > ").strip()

    if guess == "1919":
        print("\nClick. Click. Clack.")
        print("The heavy iron door opens.")
        return True
    else:
        print("\nWrong code.")
        handle_mistake()
        return False
