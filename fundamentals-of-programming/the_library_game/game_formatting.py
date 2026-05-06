def divider():
    print("\n" + "-" * 30 + "\n")


def slow_print(text, speed=0.03):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_description(text):
    wrapped_text = textwrap.fill(text, width=70)
    print(wrapped_text)
