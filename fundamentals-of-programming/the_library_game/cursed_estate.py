from game_state import handle_mistake


# This module handles the high-stakes, time-sensitive event inside The Cursed Estate.
# The player must choose the correct hiding spot to find the Photo and survive.
def explore_estate(inventory, room_data):
    print("""\nThe air in the room suddenly drops to freezing.
    The shadows stretch across the walls, and you feel a chill run down your spine.
    Veronica's eyes widen in terror. 'They are coming! Find it quickly!'""")
    print("""\nDarkens is approaching...
          Where do you look?""")

    print(
        " 1. Beneath the heavy lid of broken grand piano, the strings are twisted and tangled, but something glimmers in the darkness.")
    print(
        " 2. Under the tattered rug, the floorboards are worn and creaky, but a faint outline of a hidden compartment can be seen.")
    print(
        " 3. Inside the shattered vanity mirror, shards of glass reflect distorted images, but one piece seems to hold a secret.")

    choice = input("\nWell? Hurry! Time is running out").strip()
    if choice == "1":
        print("""\nYou reach into the darkness of the piano, your fingers brushing against the cold, twisted strings.
              Suddenly, the rusted wires snap to life, wrapping around your arm like a razor-sharp vines""")
        print("""The heavy piano lid violently slams shut, dragging you into suffocating darkness...""")
        handle_mistake()
        return False

    elif choice == "2":
        print("\nYou tear back the rug and desperately pry open the hidden floorboard compartment.")
        print("A foul, freezing wind blasts upward as the rotting floor beneath you completely gives way!")
        print("You plummet into an endless, black abyss beneath the estate...")
        handle_mistake()
        return False

    elif choice == "3":
        print("\nYou carefully reach toward the shattered vanity and peer into the jagged glass.")
        print("Tucked safely behind a loose shard, you pull out a piece of thick paper.")
        print("It is Half of a torn photo!")
        print("The creeping shadows violently recoil, hissing as they fade back into the rotting walls.")
        print("You catch your breath. You survived.")

        # Check if the room actually has the item before giving it
        item = room_data.get("item")
        if item:
            inventory.add_item(item)
            room_data["item"] = None
        return True
    else:
        # Catches invalid inputs (typos, empty enters) as a fatal hesitation
        print("\nYou hesitate, paralyzed by fear.")
        print("The shadows swallow you whole before you can make a move.")
        print("\n*** GAME OVER ***")
        handle_mistake()
        return False
