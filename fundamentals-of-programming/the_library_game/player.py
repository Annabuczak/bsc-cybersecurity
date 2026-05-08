from inventory import Inventory
from save_load import load_game
from inventory import Inventory
from movement import move_player
from rooms import rooms
from intro_riddle import print_intro
from main_menu import menu
from sanctuary_menu import sanctuary_menu
from rooms import portal
from intro_riddle import the_riddle
from rooms import secret_box
from NCP import ncp
from deadlybookpuzzle import deadlybookpuzzle
from cursed_estate import explore_estate
from inventory import take_item
from inventory import examine_items
from Blood_contract import blood_contract_puzzle
from blank_book import blank_book_puzzle
from Iron_door import iron_door_puzzle
from game_state import handle_mistake, game_flags
from game_formatting import divider
from movement import show_map
from game_state import game_flags
from game_formatting import slow_print
from rooms import portal_items
from Blood_contract import blood_contract_puzzle
from blank_book import blank_book_puzzle
from Iron_door import iron_door_puzzle


class Player:
    def __init__(self, name="Sebastian"):
        self.name = name
        self.current_room = "The Sanctuary"
        self.inventory = Inventory()

    def has_item(self, item_name):
        return self.inventory.has_item(item_name)

    def show_inventory(self):
        self.inventory.display()


def run_game(player):
    last_room = None
    while True:

        if player.current_room != last_room:
            print(f"\nYou are in the {player.current_room} room.")
            print(rooms[player.current_room].get("description", ""))
            last_room = player.current_room

        if ("Letter" in player.inventory.inventory and
                "Photo" in player.inventory.inventory and
                "Pen" in player.inventory.inventory and
                "Book" in player.inventory.inventory and
                "Newspaper" in player.inventory.inventory
        ):

            if not game_flags.get("hidden_unlocked"):
                game_flags["hidden_unlocked"] = True
                print("\nSomething shifts in the distance...")

        # THE SANCTUARY LOGIC
        if player.current_room == "The Sanctuary":

            player.inventory.display()
            action = sanctuary_menu()

            if action == "next_room":
                player.current_room = "Safe Heaven"
                print(f"\nYou are in {player.current_room}")
                print(rooms[player.current_room].get("description", ""))
                first_time_in_room = True
                handle_mistake()
                continue

            elif action == "Portal":
                portal(player.inventory)
                continue

            elif action == "The Riddle":
                the_riddle()
                continue

            elif action == "Secret Box":
                secret_box(player.inventory)
                continue

            elif action == "Enter the only open door":

                if rooms.get("Safe Heaven", {}).get("item") is None:
                    player.current_room = "The Cursed Estate"
                    print("\nThe door to Safe Heaven has sealed shut.")
                    print("A darker path opens before you...")
                    print(f"\nYou are in {player.current_room}")
                    print(rooms[player.current_room].get("description", ""))

                else:
                    player.current_room = "Safe Heaven"
                    print("\nThe door opens, and you step into the antiquarian bookshop...")

            elif action == "Door with Thousand Locks":

                if "Golden Key" in player.inventory.inventory:
                    print("\nThe locks begin to turn...")
                    player.current_room = "The Library of Forgotten Man"
                else:
                    print("\nThe door will not budge...")
                    print("You feel something is missing...")
                continue

            elif action == "Examine items":
                examine_items(player.inventory)

                if game_flags.get("hidden_unlocked"):
                    print("\nThe ground beneath you trembles...")
                    print("A hidden staircase reveals itself.")

                    choice = input("\nDo you want to descend? (yes/no): ")

                if choice == "yes":
                    player.current_room = "Forgotten Chamber"

                continue

            elif action == "Exit":
                print("\nThe shadows gather around you...")
                confirm = input("Are you sure you want to abandon the labyrinth? (yes/no) > ").strip().lower()

                if confirm == "yes":
                    print(f"\nGoodbye, {player.name}. The labyrinth will wait for your return.")
                    exit()
                else:
                    print("\nYou shake off the fear and decide to stay.")
                    continue


            elif action == "Examine items":
                examine_items(player.inventory)

            if game_flags.get("hidden_unlocked"):
                print("\nThe ground beneath you trembles...")
                print("A hidden staircase reveals itself.")
                print("\nDo you want to descend? (yes/no)")

                choice = input("> ").strip().lower()

                if choice == "yes":
                    player.current_room = "Forgotten Chamber"

            continue

        elif player.current_room == "Forgotten Chamber":

            print("\nThe chamber waits.")

            print("\nWhat would you like to do?")
            print("1. Take the vial")
            print("2. Leave it")
            print("3. Go back")

            choice = input("> ").strip()

            if choice == "1":
                print("\nYou reach for the vial…")
                print("\nIt is warm.")
                print("\nToo warm.")
                print("\nFor a moment, everything feels… lighter.")
                print("\nThen the feeling vanishes.")
                print("\nYou don't feel stronger.")
                print("You feel… noticed.")
                player.inventory.add_item("Vial of Life")
                print("\nSomewhere far above, something awakens.")

            elif choice == "2":
                print("\nYou step back.")
                print("\nNot everything is meant to be taken.")
                print("\nThe chamber feels… approving.")

            elif choice == "3":
                print("\nYou ascend the staircase.")
                player.current_room = "The Sanctuary"

            continue

        elif player.current_room == "The Library of Forgotten Man":

            slow_print("\nYou step beyond the final threshold...")

            print("\nWhat will you do?")
            print("1. Erase the story")
            print("2. Preserve it")

            choice = input("> ").strip()

            if choice == "1":
                slow_print("\nEverything fades...")
                slow_print(f"\n\"{player.name}... some stories should never be told.\"")
                print("\n*** END: Forgotten ***")
                exit()


            elif choice == "2":
                slow_print("\nYou let the story remain.")
                slow_print("\nThe pages settle.")
                slow_print("The names stop fading.")
                slow_print("\nFor the first time…")
                slow_print("they are no longer forgotten.")
                slow_print("\nThe labyrinth loosens its hold on you.")
                slow_print(f"\n\"{player.name}…\"")
                slow_print("\"You chose memory over silence.\"")
                print("\n*** END: The Keeper ***")
                exit()


        # NORMAL ROOM LOGIC
        else:
            print("\nWhat would you like to do?")
            print("People here:", ", ".join(ncp.get(player.current_room, {}).keys()) or "No one.")
            print("1. Talk")
            print("2. Look around")
            print("3. Move")
            print("4. Inventory")
            print("5. Go back to The Sanctuary")
            print("6. Examine an item")
            print("7. Show map")
            print("8. Save game")
            print("9. Exit")

            choice = input(">").strip()

            if choice == "1":
                name = input("Approach whom? ").lower().strip()
                room_ncp = ncp.get(player.current_room, {})

                if name in room_ncp:
                    chosen_ncp = room_ncp[name]
                    print(f"\nYou approach {name.lower()}!")

                    # NCP MINI LOOP
                    while True:
                        print(f"\nWhat would you like to do with {name.title()}?")
                        print("1. Talk")
                        print("2. Ask for a hint")
                        print("3. Find an item")
                        print("4. Walk away")
                        print("5. Return to The Sanctuary")

                        ncp_choice = input(">").strip()

                        if ncp_choice == "1":

                            if "questions" in chosen_ncp:
                                print(f"\nWhat do you want to ask {name.title()}?")

                                for key, q_data in chosen_ncp["questions"].items():
                                    print(f"{key}. \"{q_data['ask']}\"")
                                print("0. (Say nothing)")

                                talk_choice = input("> ").strip()

                                if talk_choice in chosen_ncp["questions"]:

                                    print(f"\nYou: \"{chosen_ncp['questions'][talk_choice]['ask']}\"")

                                    print(f"{name.title()}: \"{chosen_ncp['questions'][talk_choice]['reply']}\"")

                                elif talk_choice == "0":
                                    print("\nYou decide to hold your tongue.")
                                else:
                                    print("\nYou mumble something incomprehensible. They just stare at you.")

                            else:

                                print(f"\n{name.title()}: \"{chosen_ncp.get('dialogue', '...')}\"")


                        elif ncp_choice == "2":
                            print(f"\n{name.title()}: \"{chosen_ncp.get('hint', 'I have no advice for you.')}\"")

                        elif ncp_choice == "3":
                            item_to_give = chosen_ncp.get("gives")
                            if item_to_give and item_to_give != "None":
                                take_item_choice = input(
                                    f"Do you want to take the {item_to_give}? (yes/no): ").strip().lower()
                                if take_item_choice == "yes":
                                    player.inventory.add_item(item_to_give)
                                    print(f"\nYou received {item_to_give} from {name.title()}!")
                                    chosen_ncp["gives"] = None  # Removes the item so they can't give it twice!
                                else:
                                    print(f"\nYou declined the item from {name.title()}.")
                            else:
                                print(f"\n{name.title()} has nothing to give you right now.")

                        elif ncp_choice == "4":
                            print(f"\nYou step away from {name.title()}.")
                            break

                        elif ncp_choice == "5":
                            print(f"\nReturning to The Sanctuary.")
                            player.current_room = "The Sanctuary"
                            break

                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("No one by that name is here.")

            elif choice == "2":
                print("\nYou look around discreetly...")
                room_data = rooms.get(player.current_room, {})
                item = room_data.get("item")

                # THE DEADLY BOOK PUZZLE (SAFE HEAVEN ONLY)
                if player.current_room == "Safe Heaven" and item:
                    deadlybookpuzzle(player.inventory, player.current_room, rooms)

                # THE CURSED ESTATE PUZZLE
                elif player.current_room == "The Cursed Estate" and item:
                    explore_estate(player.inventory, rooms[player.current_room])

                # THE BLOOD CONTRACT PUZZLE
                elif player.current_room == "House of Eccentrics":
                    if "Pen" in player.inventory.inventory:
                        print("The contract is already reduced to ashes.")
                    else:
                        success = blood_contract_puzzle(player.inventory)
                        if success:
                            print("\n*** Barroso slides the Victor Hugo Pen across the table. ***")
                            player.inventory.add_item("Pen")

                # THE BLANK BOOK PUZZLE
                elif player.current_room == "The Archive of Unwritten Things" and item:
                    success = blank_book_puzzle(player.inventory, player.current_room, rooms)
                    if success:
                        rooms[player.current_room]["item"] = None


                # IRON DOOR PUZZLE
                elif player.current_room == "The Place of Torment":

                    print("\nThe corridor ends at a massive iron door.")
                    print("There is no other way forward.")
                    print("A lock waits for a 4-digit code.")

                    success = iron_door_puzzle(player.inventory)

                    if success:
                        print("\nThe door opens… but something is wrong.")
                        print("You are not allowed to pass yet.")
                        print("The labyrinth pulls you back.")
                        player.current_room = "The Sanctuary"

                        continue
                elif item:
                    search_choice = input("Would you like to search the room? (yes/no): ").strip().lower()
                    if search_choice == "yes":
                        print("Searching the room... be careful...")
                        print(f"You find something hidden: {item}")
                        player.inventory.add_item(item)
                        rooms[player.current_room]["item"] = None
                    else:
                        print("You leave the room empty-handed.")
                else:
                    print("You don't seem to find anything.")

            elif choice == "3":
                player.current_room = move_player(player.current_room, rooms)

            elif choice == "4":
                player.inventory.display()

            elif choice == "5":
                print("\nReturning to The Sanctuary.")
                player.current_room = "The Sanctuary"
            elif choice == "6":
                examine_items(player.inventory)
            elif choice == "7":
                print("\nYou are here")
                show_map(current_room=player.current_room, game_flags=game_flags)
                continue

            elif choice == "8":
                from save_load import save_game

                save_game(player, game_flags, portal_items)


            elif choice == "9":
                print("\nThe cold air of the labyrinth chills you to the bone.")
                confirm = input("Are you sure you want to abandon the labyrinth? (yes/no) > ").strip().lower()

                if confirm == "yes":
                    print(f"\nGoodbye, {player.name}. The labyrinth will wait for your return.")
                    exit()

                else:
                    print("\nYou step back from the exit, ready to continue.")
                    continue

            else:
                print("Invalid choice. Choose again.")


if __name__ == "__main__":
    # 1. Show the main menu
    choice = menu()

    if choice == "new_game":
        # Show the intro text/riddle first
        print_intro()

        # 2. Ask for the name BEFORE creating the player
        print("\nBefore we begin...")
        print("1. Enter your name")
        print("2. Continue as Sebastian")

        name_choice = input("> ").strip()

        if name_choice == "1":
            player_name = input("\nWhat is your name? ").strip()
            # If they just press Enter, default to Sebastian
            if not player_name:
                player_name = "Sebastian"
        else:
            player_name = "Sebastian"

        print(f"\nWelcome, {player_name}...")

        player = Player(name=player_name)

        run_game(player)

    elif choice == "load_game":
        from save_load import load_game

        data = load_game()

        if data:
            # Rebuild the player from the save file
            player_name = data.get("name", "Sebastian")
            player = Player(name=player_name)
            player.current_room = data.get("current_room", "The Sanctuary")

            for item, quantity in data.get("inventory", {}).items():
                for _ in range(quantity):
                    player.inventory.add_item(item)

            print(f"\nWelcome back, {player.name}...")
            print("The shadows shift as you return to the labyrinth.")

            run_game(player)

        else:
            print("\nNo saved game found. Starting a new game...")
            player = Player()
            run_game(player)

    elif choice == "exit":
        print("The labyrinth fades...")
        exit()
