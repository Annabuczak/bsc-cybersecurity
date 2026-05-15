# GLOBAL GAME STATE
# Stores variables that persist across the entre game
from game_formatting import divider

# tracks how many mistakes the player has made
mistakes = 0

# Flags used to track progress in each room (used for map visibility / logic)
game_flags = {"the_cursed_estate_done": False,
              "safe_heaven_done": False,
              "house_of_eccentrics_done": False,
              "the_archive_of_unwritten_things_done": False,
              "the_place_of_torment_done": False
              }


# Mistake handler. Called when player makes a wrong decision (e.g. puzzles)
def handle_mistake():
    global mistakes
    mistakes += 1  # increase mistake counter

    # First mistake → warning only
    if mistakes == 1:
        print("\nSomething shifts in the darkness...")
        print("You feel watched.")

    # Second mistake → game over
    elif mistakes >= 2:
        print("\nThe shadows close in.")
        print("There is no escape.")
        divider()
        print("\n*** GAME OVER ***")
        return
