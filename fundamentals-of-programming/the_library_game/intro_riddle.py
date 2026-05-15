from game_formatting import slow_print


# Game introductions
# Displays the opening narrative and sets the atmosphere of the game
def print_intro():
    current_room = "The Sanctuary"

    print("""Welcome to the Library of the Forgotten Man. You find yourself in a place that feels both familiar and strange. The air is thick with nostalgia and mystery.
You are in The Sanctuary, a vast, silent hall where shadows cling to towering shelves filled with whispering books.
The scent of old paper and leather lingers, and dim light casts eerie shapes across the walls.
This is where your journey begins. 
Here, you will uncover the mysteries of the past and confront the forgotten truths about Julian Carax—the broken writer whose soul desires only one thing… revenge.
To uncover the truth, you must solve the riddle of the Sanctuary.
Find five items. Each represents identity, love, legacy, creation, and tragedy.
Combined, they unlock the box and reveal the Golden Key.
Don’t waste precious time…
…it is time to play the game.""")


# The Sanctuary Riddle
# Provides player with cryptic clues about where to find clues
def the_riddle():
    current_room = "The Sanctuary"
    slow_print("Solve the riddle to find the truth...")
    print("...")
    slow_print("Five fragments lie where shadows keep,")
    print("In silent ink and memories deep.")
    print("...")
    slow_print("Begin where silence shelters truth")
    slow_print(" Where quiet souls are laid to rest")
    print("...")
    slow_print("A name concealed in crimson thread,")
    slow_print("A love remembered, through half is dead.")
    slow_print("...")
    slow_print("Seek next the halls where sorrow stays,")
    slow_print("A house still bound to darker days.")
    print("...")
    slow_print("Then walk where echoes twist the mind")
    slow_print("Where curious thoughts grow unconfined")
    slow_print("Where histories are written in sacred black blood")
    print("...")
    slow_print("Beyond, where words were never penned,")
    slow_print("The truths unfinished start to bend.")
    print("...")
    slow_print("A story lost, yet still your own,")
    slow_print("A truth consumed by ash and flame")
    print("...")

    slow_print("Restore the past to reclaim the name")
