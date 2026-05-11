from inventory import Inventory, examine_items
from movement import move_player, show_map
from sanctuary_menu import sanctuary_menu
from intro_riddle import the_riddle
from NCP import ncp
from deadlybookpuzzle import deadlybookpuzzle
from cursed_estate import explore_estate
from Blood_contract import blood_contract_puzzle
from blank_book import blank_book_puzzle
from Iron_door import iron_door_puzzle
from game_state import handle_mistake, game_flags
from game_formatting import slow_print
from rooms import rooms, portal, secret_box, portal_items


class Player:
    def __init__(self, name="Sebastian"):
        self.name = name
        self.current_room = "The Sanctuary"
        self.inventory = Inventory()

    def has_item(self, item_name):
        return item_name in self.inventory.inventory


def save_game_wrapper(player):
    from save_load import save_game
    save_game(player, game_flags, portal_items)


def run_game(player):
    last_room = None
    required_items = ["Letter", "Photo", "Pen", "Book", "Newspaper"]

    while True:

        # ======================
        # ROOM DISPLAY (ONLY ONCE)
        # ======================
        if player.current_room != last_room:
            print(f"\nYou are in {player.current_room}")
            print(rooms[player.current_room].get("description", ""))
            last_room = player.current_room

        # ======================
        # HIDDEN CHAMBER UNLOCK
        # ======================
        if not game_flags.get("hidden_unlocked"):
            if all(player.has_item(i) for i in required_items):
                game_flags["hidden_unlocked"] = True
                print("\n*** Something shifts in the distance... ***")

        # ======================
        # 🏛️ SANCTUARY
        # ======================
        if player.current_room == "The Sanctuary":

            print("\nYour inventory:")
            player.inventory.display()

            action = sanctuary_menu()

            if action == "next_room":
                player.current_room = "Safe Heaven"
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
                    print("\nThe safe path closes behind you...")
                else:
                    player.current_room = "Safe Heaven"
                continue

            elif action == "Door with Thousand Locks":
                if "Golden Key" in player.inventory.inventory:
                    player.inventory.remove_item("Golden Key")
                    slow_print("\nThe key trembles in your hand...")
                    slow_print("\nThe locks begin to open...")
                    player.current_room = "The Library of Forgotten Man"
                else:
                    print("\nThe door will not budge...")
                continue

            elif action == "Examine items":
                examine_items(player.inventory)

                if game_flags.get("hidden_unlocked"):
                    print("\nThe ground trembles...")
                    print("A hidden staircase reveals itself.")
                    choice = input("Descend? (yes/no): ").strip().lower()

                    if choice == "yes":
                        player.current_room = "Forgotten Chamber"

                continue

            elif action == "Save":
                save_game_wrapper(player)
                continue

            elif action == "Exit":
                print("\nGoodbye.")
                break

        # ======================
        # 🕳️ FORGOTTEN CHAMBER
        # ======================
        elif player.current_room == "Forgotten Chamber":

            print("\nThe chamber waits.")
            print("1. Take the vial")
            print("2. Leave it")
            print("3. Go back")

            choice = input("> ").strip()

            if choice == "1":
                print("\nYou take the vial...")
                player.inventory.add_item("Vial of Life")

            elif choice == "2":
                print("\nYou step back.")

            elif choice == "3":
                player.current_room = "The Sanctuary"

            continue

        # ======================
        # 📚 FINAL ROOM
        # ======================
        elif player.current_room == "The Library of Forgotten Man":

            slow_print("\nYou step beyond the final threshold...")

            print("\n1. Erase the story")
            print("2. Preserve it")

            choice = input("> ").strip()

            if choice == "1":
                slow_print("\nEverything fades...")
                print("\n*** END: Forgotten ***")
                break

            elif choice == "2":
                slow_print("\nYou let the story remain.")
                print("\n*** END: The Keeper ***")
                break

        # ======================
        # 🌍 NORMAL ROOMS
        # ======================
        else:

            print("\n1. Talk")
            print("2. Look around")
            print("3. Move")
            print("4. Inventory")
            print("5. Return to Sanctuary")
            print("6. Examine item")
            print("7. Show map")
            print("8. Save")
            print("9. Exit")

            choice = input("> ").strip()

            # ======================
            # NPC SYSTEM (FULL)
            # ======================
            if choice == "1":
                name = input("Approach whom? ").lower().strip()
                room_ncp = ncp.get(player.current_room, {})

                if name in room_ncp:
                    npc = room_ncp[name]
                    print(f"\nYou approach {name.title()}!")

                    while True:
                        print("\n1. Talk")
                        print("2. Ask for a hint")
                        print("3. Ask for an item")
                        print("4. Walk away")

                        ncp_choice = input("> ").strip()

                        if ncp_choice == "1":
                            print(f"\n{name.title()}: \"{npc.get('dialogue', '...')}\"")

                        elif ncp_choice == "2":
                            print(f"\n{name.title()}: \"{npc.get('hint', 'I have no advice for you.')}\"")

                        elif ncp_choice == "3":
                            item = npc.get("gives")

                            if item:
                                take = input(f"Take the {item}? (yes/no): ").strip().lower()

                                if take == "yes":
                                    player.inventory.add_item(item)
                                    npc["gives"] = None
                                    print(f"\nYou received {item}!")
                                else:
                                    print("\nYou decide not to take it.")
                            else:
                                print("\nThey have nothing for you.")

                        elif ncp_choice == "4":
                            print("\nYou step away.")
                            break
                else:
                    print("No one by that name is here.")

            # ======================
            # LOOK AROUND / PUZZLES
            # ======================
            elif choice == "2":
                room_data = rooms.get(player.current_room, {})
                item = room_data.get("item")

                if player.current_room == "Safe Heaven" and item:
                    deadlybookpuzzle(player.inventory, player.current_room, rooms)

                elif player.current_room == "The Cursed Estate" and item:
                    explore_estate(player.inventory, room_data)

                elif player.current_room == "House of Eccentrics":
                    if not player.has_item("Pen"):
                        if blood_contract_puzzle(player.inventory):
                            player.inventory.add_item("Pen")

                elif player.current_room == "The Archive of Unwritten Things" and item:
                    if blank_book_puzzle(player.inventory, player.current_room, rooms):
                        room_data["item"] = None

                elif player.current_room == "The Place of Torment":
                    if iron_door_puzzle(player.inventory):
                        room_data["item"] = None


                elif item:
                    take = input("Search? (yes/no): ").strip().lower()
                    if take == "yes":
                        player.inventory.add_item(item)
                        room_data["item"] = None
                        print(f"\nYou found {item}!")

                else:
                    print("Nothing found.")

            # ======================
            # MOVEMENT / UTILS
            # ======================
            elif choice == "3":
                new_room = move_player(player.current_room, rooms)
                print(f"\nYou move to {new_room}")
                player.current_room = new_room

            elif choice == "4":
                player.inventory.display()

            elif choice == "5":
                player.current_room = "The Sanctuary"

            elif choice == "6":
                examine_items(player.inventory)

            elif choice == "7":
                show_map(player.current_room, game_flags)

            elif choice == "8":
                save_game_wrapper(player)

            elif choice == "9":
                print("\nGoodbye.")
                break

            else:
                print("Invalid choice.")
