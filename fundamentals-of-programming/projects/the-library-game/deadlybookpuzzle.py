# Deadly Book Puzzle Module
# Handles the interaction in Safe Heaven (Sempere & Sons).
# The player must choose the correct book to safely obtain the Letter.
# Incorrect choices result in severe penalties via the game state manager


import time
from game_state import handle_mistake


def deadlybookpuzzle(inventory, current_room, rooms):
    print("\nYou step closer to the shelves. Three books stand out from the rest.")
    time.sleep(1.5)
    print("A strange sense of dread washes over you...")
    print("Choose the wrong one, and you may never leave this place again.")

    print("\n1. The Book of Shadows")
    print("2. The Book of Light")
    print("3. The Book of Secrets")
    print("4. Walk away... empty-handed")

    # Fixed the input syntax error and added a clear prompt
    book_choice = input("\nWhich book do you choose? > ").strip()

    # Present player with choices
    if book_choice == "1":
        print("\n--- The Book of Shadows ---")
        time.sleep(1.5)
        print("As you open the book, a dark mist envelops you.")
        print("You feel your consciousness slipping away, and the world around you fades into darkness.")
        print("You have been consumed by the shadows, your fate sealed within the pages.")

        # Standardized failure state
        handle_mistake()
        return False

    elif book_choice == "2":
        print("\n--- The Book of Light ---")
        time.sleep(1.5)
        print("You carefully slide The Book of Light off the shelf.")
        print("As you open it, a warm glow fills the room. You feel a surge of hope and clarity.")
        print("Hidden between the yellow pages, you find a sealed envelope!")

        # Add item and update room state safely
        inventory.add_item("Letter")
        if current_room in rooms:
            rooms[current_room]["item"] = None

        # Standardized success message
        print("\n*** You obtained the Letter! ***")
        return True

    # instant game over
    elif book_choice == "3":
        print("\n--- The Book of Secrets ---")
        time.sleep(1.5)
        print("As you open the book, a chilling wind sweeps through the room.")
        print("You feel an overwhelming sense of fear and unease, as if unseen eyes are watching you.")
        print("The secrets within the book consume your mind, leaving you trapped in a nightmare.")
        print("\n*** GAME OVER ***")

        # Standardized failure state (replaced exit() with handle_mistake)
        handle_mistake()
        return False

    # Safe exit
    elif book_choice == "4":
        print("\nYou step back, deciding to leave the books undisturbed.")
        print("Perhaps you are not ready for their secrets yet.")
        return False

    else:
        # Catches typos or invalid numbers
        print("\nYou hesitate, unsure of which book to choose.")
        print("The moment passes, and the opportunity slips away.")
        print("You step back from the shelf.")
        return False
