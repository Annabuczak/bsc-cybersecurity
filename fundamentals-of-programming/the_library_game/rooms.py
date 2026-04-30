def the_sanctuary(inventory):
    while True:
        print("\nSebastian, don't be afraid. The place you dreamed about is real...Welcome to The Sanctuary")
        print("Please look around you, choose one item")
        print("Portal")
        print("The Riddle")
        print("Secret Box")
        choice = input("> ").strip().lower()
        if choice == "Portal":
            print("Leave what you have found here")
        elif choice == "The Riddle":
            print("Solve the riddle to find the truth...")
            the_riddle()
        elif choice == "Secret Box":
            print("When the fragments are restored, the box that once held past, reveles the key to what awaits")
        elif "box" in choice:
            print("You open the box and find The Golden Key")
        elif choice == "Open the door of your choice":
            print("The door opens, and you step into the next chapter of your journey...")
        elif choice == "Stay in The Sanctuary":
            print("Wake up, Sebastian")
            break
        else:
            print("See you in your next dream Sebastian...")


def portal(inventory):
    required_items = ["Letter", "Photo", "Pen", "Book", "Newspaper"]
    if all(item in inventory.inventory for item in required_items):
        print("You have entered the portal!")
    else:
        print("I'm afraid you can't go any further, Sebastian.")
        return
    while True:
        print("welcome back...")
        choice = input("Would you like to open the box and find the truth? (yes/no) ").strip().lower()
        if choice == "yes":
            print("open the box and find the truth...")
        elif choice == "no":
            print("You are not ready to face the truth, Sebastian. The Game ends here for you. Farewell.")
            break
        elif choice == "x":
            break
        else:
            print("Invalid choice.")


def secret_box(inventory):
    required_items = ["Letter", "Photo", "Pen", "Book", "Newspaper"]
    if all(item in inventory.inventory for item in required_items):
        print("When the fragments are restored...")
        print("Open the box and find The Golden Key")
    else:
        print("You are not ready to face the truth, Sebastian.")


rooms = rooms = {
    "The Sanctuary": {
        "north": "Safe Heaven",
        "item": None,

    },

    "Safe Heaven": {
        "south": "The Sanctuary",
        "east": "The Cursed Estate",
        "item": "Letter",
        "description": """You step into Sempere & Sons, a narrow antiquarian bookshop where dust drifts in the light.
The air smells of leather and rain-soaked paper, shelves leaning as if listening.
Mr Sempere watches from behind the counter, while Daniel rearranges books nearby.
The bell above the door hangs still, yet the shop feels guarded,
as if a secret is close to being uncovered.
Mention Julian Carax and a hesitation flickers,
a glance exchanged too quickly.
Somewhere among the books, a clue waits in plain sight.
One volume sits slightly apart from the others, its spine marked only with the initials JC.
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
As she speaks, her gaze drifts toward a cracked frame on the wall.
The photograph inside is torn… but not completely."""

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
    }
}

items = ["Portal", "The Riddle", "Secret Box"]
portal_items = []
items_needed = ["Letter", "Photo", "Pen", "Book", "Newspaper"]
