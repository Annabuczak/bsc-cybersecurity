def blood_contract_puzzle(inventory, current_rooms, rooms):
    print("""\nYou approach a glowing parchment pinned to the centre of the wall.
    It is a contract binding the soul of Julian Carax, but the final word is blank.""")

    if "Pen" not in inventory:
        print("You try to wrote missing word with your finger, but nothing happens")
        print("You need something to wrote it with...something special")
        return

    print("You pull out the Pen Diego Barroso gave you.")
    print("As you press the nib to the paper, ink is read. Red like your blood")

    health = 3

    acceptable_words = ["fire", "flame", "flames", "ash", "ashes"]

    while health > 0:
        print(f"\n[Blood remining: {'heart' * health}]")
        guess = input("\nWhat do you write? >...").stip().lower()

        if guess in acceptable_words:
            print(f"\nAs you press the nib to the paper, {guess.lower}, the contract ignites in fire!")
            print("The ashes scatter, breaking the bind on Julian's soul")
            print("You have survived")
            return

        else:
            health -= 1
            if health > 0:
                print(f"\nThe word {guess.lower()} burns away on the paper.")
                print("The pen bites deeper into your skin, drawing more blood.")
                print("You feel dizzy. That is the wrong word")

            else:
                print(f"\nThe word {guess.lower()} burns away.")
                print("The pen drains the last of your blood")
                print("You collapse to the floor.The Shadow of The Wind consume you...")
                print("\n GAME OVER")
