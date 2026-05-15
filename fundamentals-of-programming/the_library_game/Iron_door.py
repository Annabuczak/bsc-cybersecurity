# Iron Door Puzzle Module
# Handles the final barrier in The Place of Torment.
# The player must recall the date of the Aldaya fire (1919) from the Newspaper lore.


import time
from game_state import handle_mistake


# Handles the final barrier in The Place of Torment.
# The player must recall the date of the Aldaya fire (1919) from the Newspaper
def iron_door_puzzle(inventory):
    print("\nThe heavy iron door stands before you, cold and unyielding.")
    time.sleep(1.5)
    print("A rusted mechanical lock waits for a 4-digit code.")

    guess = input("\nEnter the 4-digit code: > ").strip()

    if guess == "1919":
        # Added dramatic timing for the unlocking sequence
        print("\n...")
        time.sleep(1)
        print("Click.")
        time.sleep(1)
        print("Click.")
        time.sleep(1)
        print("Clack.")
        time.sleep(1.5)

        print("\nThe heavy iron door groans as it slowly swings open.")
        print("The path forward is clear.")
        return True

    else:
        print("\nThe lock jams with a harsh, metallic grind.")
        time.sleep(1.5)
        print("Inspector Varela shakes his head in the shadows. 'Wrong.'")

        # Standardized failure state
        handle_mistake()
        return False
