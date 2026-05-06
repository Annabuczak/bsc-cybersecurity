def iron_door_puzzle(inventory):
    print("""f\n As you step away from the shadows and approach the heavy, rusty iron door
    A thick layer of old, cold ahs covers mechanical combination lock.
    All you need to crack it is a 4-digit code.""")

    if "Newspaper" not in inventory.inventory:
        print("""\n You wipe away the ash, but the numbers mean nothing to you.
        Perhaps there is a clue you are missing...
        ....someone here might know about the fire""")
        return False

    print("""\nYou pull out the scorched newspaper clipping Inspector Varela gave you.
    The tragic Aldaya fire....The lock seems to require the year it happened.""")

    attempts = 3
    while attempts > 0:
        guess = input("\nEnter the 4-digit code: ")

        if guess == "1919"
            print("***CRACK**")
            print("""\nThe heavy iron mechanism grind together, and the door slowly open.
            The ash clears from the air. A cold draft washes over you.
            You have uncovered the final truth.
            Its time to return to The Sanctuary and open The Portal""")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print("\nThe lock doesnt budge. A cold wind howls through the cell.")
                print("You have {attempts} attempt(s) left to solve it.".format(attempts=attempts))

            else:
                print("""\n***CRUNCH***
                The lock jams permanently. The iron door is sealed forever.
                The shadow of Montjuc Castle close in.
                All that is left is The Shadow of The Wind.""")
                print("\nGAME OVER")
                exit()
