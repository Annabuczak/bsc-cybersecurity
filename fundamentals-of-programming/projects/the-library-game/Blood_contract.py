from game_state import handle_mistake


# Blood Contract Puzzle Module
# Handles the interaction in the House of Eccentrics.
def blood_contract_puzzle(inventory):
    print("\nYou approach a glowing parchment pinned to the center of the wall.")
    print("It is a contract binding the soul of Julian Carax.")
    print("The final sentence reads: 'I bind my soul to the shadows, never to rest,")
    print("until the ________ consumes my final word.'")

    # Thematic mechanic explanation
    print("\nYou pull out the Silver Pen Diego Barroso gave you.")
    print("As you press the nib to the paper, it doesn't use ink. It draws your own blood.")

    # Acceptable correct answers (flexible input)
    acceptable_words = ["fire", "flame", "flames", "ash", "ashes"]

    # Input loop
    while True:
        guess = input("What word do you write? > ").strip().lower()

        if guess in acceptable_words:
            print("\nThe word burns away on the paper. The contract dissolves into smoke.")
            print("Barroso’s eyes widen in genuine respect.")
            print("\n'Well played, Sebastian,' he whispers.")
            return True

        else:
            print("\nBarroso laughs cruelly. 'Wrong. You understand nothing.'")
            print("The shadows in the room seem to grow longer...")
            handle_mistake()
            return False
