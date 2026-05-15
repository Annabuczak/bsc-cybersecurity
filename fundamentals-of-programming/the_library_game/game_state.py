# GLOBAL GAME STATE
# Stores variables that persist across the entre game
from game_formatting import divider

# tracks how many mistakes the player has made
mistakes = 0

# Flags used to track progress in each room (used for map visibility / logic)
DEFAULT_GAME_FLAGS = {
    "the_cursed_estate_done": False,
    "safe_heaven_done": False,
    "house_of_eccentrics_done": False,
    "the_archive_of_unwritten_things_done": False,
    "the_place_of_torment_done": False,
    "hidden_unlocked": False,
    "box_opened": False,
    "game_over": False,
}

game_flags = DEFAULT_GAME_FLAGS.copy()


def reset_game_flags():
    global mistakes
    mistakes = 0
    game_flags.clear()
    game_flags.update(DEFAULT_GAME_FLAGS)


# Mistake handler. Called when player makes a wrong decision (e.g. puzzles)
def handle_mistake():
    global mistakes
    mistakes += 1  # increase mistake counter

    # First mistake → warning only
    if mistakes == 1:
        print("\nSomething shifts in the darkness...")
        print("You feel watched.")
        return False

    # Second mistake → game over
    elif mistakes >= 2:
        print("\nThe shadows close in.")
        print("There is no escape.")
        divider()
        print("\n*** GAME OVER ***")
        game_flags["game_over"] = True
        return True
