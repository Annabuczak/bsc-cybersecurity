
# The Library Game

A text-based Python adventure game built for the Fundamentals of Programming module.

The game is organised across multiple modules for rooms, movement, player state, inventory, puzzles, menus, and save/load behaviour.

## Running The Game

From this folder:

```bash
python3 main.py
```

## Structure

- `main.py` - Entry point and main menu.
- `player.py` - Player actions and main game loop.
- `rooms.py` - Room descriptions, navigation, and room items.
- `movement.py` - Movement logic.
- `inventory.py` - Inventory handling.
- `game_state.py` - Game flags and progress state.
- `save_load.py` - Save/load support.
- `main_menu.py` and `sanctuary_menu.py` - Menu handling.
- Puzzle and story modules:
  - `intro_riddle.py`
  - `deadlybookpuzzle.py`
  - `blank_book.py`
  - `Blood_contract.py`
  - `Iron_door.py`
  - `NCP.py`
  - `cursed_estate.py`

## Skills Practised

- Breaking a larger program into modules
- Functions and control flow
- Dictionaries and lists
- Inventory and game-state tracking
- Basic save/load design
- User input handling
