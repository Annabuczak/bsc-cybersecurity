# NCP.py

ncp = {
    "Safe Heaven": {
        "sempere": {
            "dialogue": """Sempere studies you quietly. 
"Looking for something...or someone?" he asks.
Before you can answer, Daniel shifts beside him.
"Father..." he whispers, uneasy. But Sempere seems not to hear.
His eyes are still on you.
"Books remember more than people do," he says softly, almost to himself. 
"Some books are not meant to be found twice" He says as he walks away.""",
            "hint": "Daniel looks at you, then at the books on the shelf",
            "gives": None,
            "questions": {
                "1": {
                    "ask": "Who is Julian Carax?",
                    "reply": "A ghost, my boy. A man erased from history."
                },
                "2": {
                    "ask": "What do the books remember?",
                    "reply": "Everything we try to forget. The dust settles, but the ink remains."
                },
                "3": {
                    "ask": "What are you hiding?",
                    "reply": "Nothing that concerns you, child. Leave the past where it lies."
                }
            }
        },
        "daniel": {
            "dialogue": """Daniel speaks quietly.
"I...I don't know much about Julian Carax, but I know his story hasn't ended yet..."
He takes a deep breath in and looks around to see where his father has gone to.
"Be careful, fate is a funny thing that doesn't always work the way we want it to..." he says before following his father.""",
            "hint": "Daniel looks at you, then at the books on the shelf.",
            "gives": None,
            "questions": {
                "1": {
                    "ask": "Why is your father so afraid?",
                    "reply": "He's not afraid. He's guilty. We all are."
                },
                "2": {
                    "ask": "Where did Julian go?",
                    "reply": "Only the shadows know. And they don't give up their secrets easily."
                },
                "3": {
                    "ask": "What do you mean about fate?",
                    "reply": "Just what I said. The ending is already written. You are just turning the pages."
                }
            }
        },
    },

    "The Cursed Estate": {
        "veronica": {
            "dialogue": """Veronica looks at you with tired eyes, her voice barely above a whisper.
"I was an old maid to my beautiful Penelope.
I loved her like a daughter, but she was never mine to keep.
Penelope was a wild spirit, always chasing dreams too big for her.
Julian Carax was her true love, but their love had to be hidden.
They married in secret… but it was a tragedy waiting to happen.
I still remember the day they left. It felt like a storm had torn through the house.
She was happy… but I knew it would end badly.
And it did.
They disappeared without a trace.
And I never saw her again." """,
            "hint": "The house remembers...and it is hungry. Find her face in the cracked glass before the shadow takes you",
            "gives": None,
            "questions": {
                "1": {
                    "ask": "Why was their love a tragedy?",
                    "reply": "Some bloodlines are cursed to never mix. They found out the terrible truth too late."
                },
                "2": {
                    "ask": "Where did they go?",
                    "reply": "If I knew, my heart wouldn't be broken. They vanished into the smoke."
                },
                "3": {
                    "ask": "What happened to this house?",
                    "reply": "Sorrow ate it from the inside out. The walls breathe with her memory."
                }
            }
        }
    },

    "House of Eccentrics": {
        "barroso": {
            "dialogue": """Diego Barroso smiles, his teeth stained with the finest Rioja money can buy.
"Julian? He signed his life away for a ghost, he had a real talent, what a shame he threw it all away."
He gives you a pen. "You see this pen boy? Great Victor Hugo used it to write Les Miserables."
"Take it. Perhaps you can finish the story... But ink won't work." """,
            "hint": "He spins a pen between his fingers, watching you closely. The contract must be fulfilled.",
            "gives": None,
            "questions": {
                "1": {
                    "ask": "What contract are you talking about?",
                    "reply": "A binding of souls! A masterpiece of despair!"
                },
                "2": {
                    "ask": "Why won't ink work?",
                    "reply": "Because ink is cheap! The shadows demand currency of a much higher value. The currency of life."
                },
                "3": {
                    "ask": "Who holds Julian's contract?",
                    "reply": "The labyrinth itself. And it does not like to let things go."
                }
            }
        }
    },

    "The Archive of Unwritten Things": {
        "girl": {
            "dialogue": """The girl does not speak. 
Her eyes are dark, reflecting a sadness that words could never capture.
She slowly raises a pale, trembling finger and points toward the narrow lectern in the center of the room.
She is waiting for you to read.""",
            "hint": "You hear a faint whisper in your mind, like the rustling of dry leaves: 'The pages will lie to you at first. Wait for the final truth... and remember it exactly as it is written.'",
            "gives": None,
            "questions": {
                "1": {
                    "ask": "Who are you?",
                    "reply": "(She tilts her head, her eyes welling with black tears, but says nothing.)"
                },
                "2": {
                    "ask": "Did you know Penelope?",
                    "reply": "(She points a trembling finger at the blank book.)"
                },
                "3": {
                    "ask": "How do I escape?",
                    "reply": "(She shakes her head slowly, pointing down at the shadows creeping at your feet.)"
                }
            }
        }
    },

    "The Place of Torment": {
        "varela": {
            "dialogue": """Inspector Varela leans against the damp stone wall, his eyes hollow and empty.
"You made it this far, Sebastian. But the truth is locked away behind that heavy iron door."
He holds out a scorched piece of paper, his hand trembling.
"This is all that survived the Aldaya fire. The answer you need is in the ashes. 
Read it carefully." """,
            "hint": "The combination lock to the cell door requires four digits... the year the Aldaya estate burned to the ground.",
            "gives": "Newspaper",
            "questions": {
                "1": {
                    "ask": "What happened in the Aldaya fire?",
                    "reply": "Hell on earth, Sebastian. Everything burned. Everyone burned."
                },
                "2": {
                    "ask": "What is behind that iron door?",
                    "reply": "The end of the story. The thing we've all been running from."
                },
                "3": {
                    "ask": "Why are you locked in here?",
                    "reply": "I'm not locked in. I'm standing guard. Making sure it doesn't get out."
                }
            }
        }
    }
}
