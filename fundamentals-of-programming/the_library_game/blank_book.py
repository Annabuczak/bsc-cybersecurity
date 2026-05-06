import time


def blank_book_puzzle(inventory, current_room, rooms):
    print(f"""\nYou approach the narrow lectern. The book is open.
          The Ghost Girl watches you from the shadows, 
          her pale finger pointing at the pages.
          The ink on the paper begins to writhe and shift like a living smoke.
          Pay close attention.""")

    time.sleep(3)
    print("\n" * 50)

    print("The pages flutter...a sentence form:")
    print(">>> Julian Carax was erased.<<<")
    time.sleep(2.5)
    print("\n" * 50)

    print("The final truth burns onto the page:")
    print(">>> The story was never gone, only hidden. <<<")
    time.sleep(3.5)
    print("\n" * 50)

    print("The book suddenly slams shut!")
    print("The Ghost Girl steps forward, waiting for you to speak the final truth.")

    guess = input("\nType the final sentence exactly: > ").strip().lower()
    clean_guess = guess.replace(".", "").replace(",", "")

    if clean_guess == "the story was never gone, only hidden":
        print("\nThe Ghost Girl gives a sad, quiet smile and fades into the mist.")
        print("The book rests silently on the lectern. It belongs to you now.")
        inventory.add_item("Book")
        print("\n*** You obtained the Nameless Book! ***")
        return True
    else:
        print("\nThe Ghost Girl's eyes go black. The shadows surge forward with a deafening shriek!")
        print("You are violently thrown backwards, forced away from the lectern.")
        print("That was the wrong truth. You will have to try again.")
        return False
