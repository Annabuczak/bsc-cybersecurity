# This module acts as a spatial database. It defines the map
# using dictionary based graph data structure
# and contains the logic for interactive environmental objects
# within The Hub word

# Global game data
# Items available in The Sanctuary menu.
items = ["Portal", "The Riddle", "Secret Box"]
# Stores items thrown into the portal, used to unlock The Secret Box.
portal_items = []
# Required items needed to open Secret Box and to retrieve Golden Key
items_needed = ["Letter", "Photo", "Pen", "Book", "Newspaper"]
# Special item foung in the hidden chamber
item_found_in_hidden = ["Vial of Life"]

from game_state import game_flags


# Sanctuary, The Hub of the game
# Handles the unique text-based interface for the game.
# Parses user input and returns standardised command strings to the main game engine.

def the_sanctuary(inventory):
    # We use a while loop just in case they type gibberish.
    # It traps them here until they type a valid command.y(inventory):

    # Continuous loop until player leaves Sanctuary
    while True:
        print("\nSebastian, don't be afraid. The place you dreamed about is real...Welcome to The Sanctuary")
        print("Please look around you, choose one item")
        print("Portal")
        print("The Riddle")
        print("Secret Box")
        print("Open the door")
        print("Stay in The Sanctuary")

        # Get user input and normalise it
        choice = input("> ").strip().lower()
        if choice == "portal":
            portal(inventory)
            print("Leave what you have found here")
        elif choice == "the riddle":
            print("Solve the riddle to find the truth...")
            the_riddle()
        elif choice == "secret box":
            print("When the fragments are restored, the box that once held past, reveles the key to what awaits")

        elif "door" in choice:
            print("The door opens, and you step into the next chapter of your journey...")
            break
        # Exit game
        elif "stay" in choice:
            print("Wake up, Sebastian")
            exit()

        # Invalid input
        else:
            print("See you in your next dream Sebastian...")


# Portal functions
# Portal allows player to drop items found in Rooms and to open The Secret Box
def portal(inventory):
    # Handles the interactive Portal mechanics.
    # Allows players to transfer items from their personal inventory into
    # the portal's global state, tracking progress toward the endgame condition.
    print("\nThe Portal hums with a strange energy...")
    print("It feels as if you are being pulled to throw certain items into it...")

    # If there are no items player cannot use The Portal
    if not inventory.inventory:
        print("Your pockets are empty. You must leave The Portal.")
        return

    print("Your current items:")
    inventory.display()

    choice = input("\nDo you want to throw an item into the portal? (yes/no): ").strip().lower()

    if choice == "no":
        print("\nCome back when you are ready to put items inside The Portal.")

    elif choice == "yes":
        # Format input to title case to match inventory keys exactly
        item_choice = input("Which item do you want to throw in? ").strip().title()

        # If player has items -> remove and store in The Portal
        if item_choice in inventory.inventory:
            print(f"\nYou toss the {item_choice} into the portal...")
            inventory.remove_item(item_choice)
            portal_items.append(item_choice)

            # Check if the player has successfully submitted all required items
            if all(item in portal_items for item in items_needed):
                print("\n*** The portal awakens... The Secret Box is ready to be opened. ***")
        else:
            print(f"\nYou don't have a {item_choice} to throw.")


# Evaluates if the player has met all the requirements
# If The Portal conditions are met, player receives The Golden Key.
def secret_box(inventory):
    required_items = ["Letter", "Photo", "Pen", "Book", "Newspaper"]

    if game_flags.get("box_opened"):
        print("\nThe box is empty now.")
        print("Whatever it held… is already yours.")
        return
    # Validate that all required items exist within the portal_items list
    if all(item in portal_items for item in required_items):
        print("\nThe box begins to tremble.")
        print("The air around you tightens.")
        print("\nThe things you sacrificed… are not gone.")
        print("They are remembered.")
        print("\nThe lid unlocks with a slow, deliberate sound.")
        print("\nInside, resting in silence…")
        print("\nA key.")
        print("\nNot shining.")
        print("Not inviting.")
        print("Waiting.")

        # Give player The golden Key
        inventory.add_item("Golden Key")

        # Mark as open
        game_flags["box_opened"] = True

        print("\n*** You obtained the Golden Key ***")

    else:
        print("\nThe box remains still.")
        print("It knows you are not ready.")


# The labyrinth is structured as a dictionary of dictionaries.
# Each key is a room name, mapping to its available exits, discoverable items,
# and narrative description. This structure allows O(1) time complexity
# when looking up room data during the main loop.

rooms = {
    # Starting location
    "The Sanctuary": {
        "north": "Safe Heaven",
        "item": None,

    },

    "Safe Heaven": {
        "south": "The Sanctuary",
        "east": "The Cursed Estate",
        "item": "Letter",
        "description": """The Sanctuary You step into Sempere & Sons, a narrow antiquarian bookshop where dust drifts in the light.
The air smells of leather and rain-soaked paper, shelves leaning as if listening.
Mr Sempere watches from behind the counter, while Daniel rearranges books nearby.
The bell above the door hangs still, yet the shop feels guarded,
as if a secret is close to being uncovered.
Mention Julian Carax and a hesitation flickers,
a glance exchanged too quickly.
Somewhere among the books, a clue waits in plain sight.
One volume sits slightly apart from the others.
It doesn’t seem to belong where it is."""
    },

    "The Cursed Estate": {
        "west": "Safe Heaven",
        "north": "House of Eccentrics",
        "item": "Photo",
        "description": """Avenida del Tibidabo 32, once a grand mansion, a shrine to wealth.
Now it stands cracked and hollow, windows blind with grime and ivy.
Inside, damp air smells of mould, sour perfume, and cold ash.
Velvet curtains lie torn, chandeliers hang askew,
and every step stirs the groan of rotten boards.
Portrait eyes follow you through silent corridors.
Something still lingers, old secrets in the walls,
a tragedy that never quite faded.
Another fragment lies hidden here.
Veronica, the old maid , she waits for her long lost little girl to come back home... Ask her about Penelope,
a forbidden love and a secret wedding that ended in tragedy.
"""

    },

    "House of Eccentrics": {
        "south": "The Cursed Estate",
        "north": "The Archive of Unwritten Things",
        "item": "Pen",
        "description": """You push through the café doors into a haze of smoke and murmured arguments.
The House of Eccentrics hums with uneasy energy, laughter in the wrong places,
whispers that die as you pass. Writers, poets, and antiquarians crowd the tables,
trading rumours like rare books.
The air tastes of burnt coffee, cheap brandy, and rain-soaked coats.
Walls are layered with manifestos and quotes pinned like evidence.
Somewhere in the noise, a clue to Julian Carax’s past waits to be uncovered.
Sebastian,go to Diego Barroso.
He watches you already, a faint smile behind his glass.
In his hand, he turns a pen slowly between his fingers,
not absent-mindedly, but deliberately.
As if waiting for you to ask."""
    },

    "The Archive of Unwritten Things": {
        "south": "House of Eccentrics",
        "north": "The Place of Torment",
        "item": "Book",
        "description": """A room without shelves, only their absence. The air is thick with untold endings,
and the walls shimmer like water. As you step forward, words bloom in the dark:
chapters never written, titles never published, names never allowed to exist.
In the shadows, a young girl flickers into view, pale and unsteady.
She says nothing, only watches, then slowly raises her hand and points.
Follow her.
A narrow lectern stands ahead. A single book lies open,
It's a sentence repeating, changing by a word each time you blink.
Sebastian, go to the lectern. Search it.
An old book waits, one that seems to recognise you.
As you lift it, the room falls silent.
When you look back, the girl is gone."""
    },

    "The Place of Torment": {
        "south": "The Archive of Unwritten Things",
        "east": "The Library of Forgotten Man",
        "item": "Newspaper",
        "description": """You have come far, Sebastian.
Montjuïc Castle rises at dusk, its stone walls swallowing the last light.
The fortress looms over Barcelona, a warning from the war, its corridors thick with damp iron and old smoke.
A man steps from the darkness. Inspector Manuel Varela, a ruin of power.
His hands tremble as he speaks of orders obeyed, doors broken, names erased.
“I thought fear could keep a city quiet,” he whispers, “but it only taught it to mourn.”
From his coat, he draws a scorched newspaper clipping.
“Penelope. Fire. Suspicious.”
The clipping trembles slightly in his hand.
Even before he offers it, you know this is something you cannot leave behind
“Find the truth” he says, and let the dead finally sleep.
When you look back, he is gone.
And the silence feels heavier than before."""

    },
    # Final room
    "The Library of Forgotten Man": {
        "west": "The Place of Torment",
        "item": None,
        "description": """ The Sanctuary waits.
One by one, the fragments find their place in the stone:
the letter marked JC, the torn photograph, the pen,
the nameless book, the scorched clipping.
Each settles with quiet certainty.

At the base, a sealed box exhales dust and opens.
Inside, the treasure you were looking for the Golden Key.
The door yields slowly.
Beyond it, the air carries ash, roses, and old paper.

The Library of Forgotten Man stretches into fog.
On a lectern lies the missing half of the photograph,
Penelope’s face restored, Julian’s hand in hers.
Not lost. Taken.

Beside it, a worn leather book.
His name inside. Hers beneath it.

As the pages turn, the truth gathers:
Julian Carax was erased.
His words hunted.
Penelope silenced.
On the final page, the same seal appears—no longer broken, but whole.

You understand now.
This place was waiting.

The story was never gone,only hidden.

Behind you, the labyrinth loosens its hold.
The door does not close.

It simply lets you go."""
    },
    # Hidden chamber
    "Forgotten Chamber": {
        "up": "The Sanctuary",
        "item": "Vial of Life",
        "description": """You descent a narrow, spiraling stone staircase, that isn't on any map.
        A place beyond memory. It should not exist.
        In the center of the room rests a small silver pedestal
        There is a sense of absolute peace here... a temporary refuge from the shadow.
        Don't be fooled. The darkens awaits."""

    }
}
