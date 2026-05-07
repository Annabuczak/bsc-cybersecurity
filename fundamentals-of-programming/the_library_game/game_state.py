# GLOBAL GAME STATE
mistakes = 0

game_flags = {"safe_heaven_done": False,
              "estate_done": False,
              "eccentrics_done": False,
              "archive_done": False,
              "torment_done": False
              }

# GLOBAL VARIABLES
mistakes = 0


def handle_mistake():
    global mistakes
    mistakes += 1

    if mistakes == 1:
        print("\nSomething shifts in the darkness...")
        print("You feel watched.")
    elif mistakes >= 2:
        print("\nThe shadows close in.")
        print("There is no escape.")
        print("\n*** GAME OVER ***")
        exit()
