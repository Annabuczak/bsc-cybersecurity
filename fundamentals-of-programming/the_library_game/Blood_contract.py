def blood_contract_puzzle(inventory):
    print("\nYou approach a glowing parchment pinned to the center of the wall.")
    print("It is a contract binding the soul of Julian Carax.")
    print("The final sentence reads: 'I bind my soul to the shadows, never to rest,")
    print("until the ________ consumes my final word.'")

    if "Pen" not in inventory.inventory:
        print("\nYou try to write the missing word with your finger, but nothing happens.")
        print("You need something to write with... something special.")
        return False

    print("\nYou pull out the Silver Pen Diego Barroso gave you.")
    print("As you press the nib to the paper, it doesn't use ink. It draws your own blood.")

    acceptable_words = ["fire", "flame", "flames", "ash", "ashes"]

    while True:
        guess = input("What word do you write? > ").strip().lower()

        if guess in acceptable_words:
            print(
                f"\nAs you trace the word '{guess.lower()}', the contract ignites in a flash of cold, blue fire!")
            print("The ashes scatter, breaking the bind on Julian's soul.")
            print("You have survived the House of Eccentrics.")
            return True

        else:
            print(f"\nThe word '{guess.lower()}' burns away on the paper.")
            print("The pen bites deeper into your skin, drawing more blood.")
            print("You feel dizzy. That is the wrong word.")
            handle_mistake()
