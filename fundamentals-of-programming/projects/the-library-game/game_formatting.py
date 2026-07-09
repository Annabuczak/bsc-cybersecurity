import sys
import time
import os
import textwrap


# Visual divider
# Prints a horizontal line t separate sections of text in the game UI
def divider():
    print("\n" + "=" * 30 + "\n")


# Typewriter effect
# Prints text character-by-character for dramatic storytelling
# 'speed' controls delay between characters (lower = faster)
def slow_print(text, speed=0.03):
    try:
        for character in text:
            sys.stdout.write(character)  # Prints one character
            sys.stdout.flush()  # Force it to display immediately
            time.sleep(speed)  # Pauses between haracter
        print()  # Moves to next line after finishing
    except KeyboardInterrupt:  # If player presses ctrl + c, skip animation and print instantly
        print(text)


# Clear terminal screen depending on operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Wraps long text so it fits in terminal
def print_description(text):
    wrapped_text = textwrap.fill(text, width=70)
    print(wrapped_text)
