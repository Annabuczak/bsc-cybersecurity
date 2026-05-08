from game_state import handle_mistake


def deadlybookpuzzle(inventory, current_room, rooms):
    print("""\nYou step closer to the shelves. Three books stand out from the rest.
                A strange sense of dread washes over you...choose the wrong one, 
                and you may never leave this place again.""")
    print("1. The Book of Shadows")
    print("2. The Book of Light")
    print("3. The Book of Secrets")
    print("4. Walk away...empty-handed")

    book_choice = input(...).strip()

    if book_choice == "1":
        print("\nThe Book of Shadows")
        print("""As you open the book, a dark mist envelops you. 
        You feel your consciousness slipping away, and the world around you fades into darkness.
        You have been consumed by the shadows, and your fate is sealed within the pages of the book.""")
        handle_mistake()
        return False
    elif book_choice == "2":
        print("""\nYou carefully slide The Book of Light off the shelf. 
        As you open it, a warm glow fills the room, and you feel a surge of hope and clarity.
        Hidden between the yellow pages, you find a sealed Letter!
        It is exactly what you were looking for.""")

        inventory.add_item("Letter")
        if current_room in rooms:
            rooms[current_room]["item"] = None
        print("you take the Letter")

    elif book_choice == "3":
        print("""\nAs you open the book, a chilling wind sweeps through the room. 
        You feel an overwhelming sense of fear and unease, as if unseen eyes are watching you.
        The secrets within the book consume your mind, leaving you trapped in a never-ending nightmare.""")
        print("\n***GAME OVER***")
        exit()

    elif book_choice == "4":
        print("""\nYou decide to walk away, leaving the books undisturbed.""")

    else:
        print("""\nYou hesitate, unsure of which book to choose.
        The moment passes, and the opportunity slips away.
        You are left with a lingering sense of what could have been.""")
