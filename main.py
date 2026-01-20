import random as r
from colorama import init, Fore, Style
import os
import time
import json
import datetime as dt
init(autoreset=False)

def cls() -> None:
    os.system('cls' if os.name=='nt' else 'clear')

def print_info() -> None:
    cls()
    print(f"{Fore.CYAN}########################################")
    print("🎰 Element's Slot Machine 🎰 ver: 1.0.0")
    print(f"########################################\n\n{Fore.RESET}")

def print_ui() -> None:
    cls()
    print_info()
    if game_state == "menu":
        print(f"Current Balance 💲: {money}")
        print(f"Press {str(PULL_KEYBIND_TEXT)} to spin or press {EXIT_KEYBIND_TEXT} to EXIT")
    elif game_state == "pulling":
        print("Game state pulling")
    elif game_state == "result":
        print(f"Current Balance 💲: {money} + {temp_money}")
    else:
        print(f"{Fore.RED} Error in print_ui function, invalid game_state")


def generate_player_data() -> None:
    default_data: dict[str, str] = {"money":"50","last income":f"{dt.datetime.now()}"}
    with open("player.json", "w") as file:
        json.dump(default_data, file, indent=4)
    print("created player file")

def save_player_data() -> None:
    save_data: dict[str, str] = {"money":f"{money}","last income":f"{dt.datetime.now()}"}
    with open("player.json", "w") as file:
        json.dump(save_data, file, indent=4)
    print(f"{Style.DIM}%saved player data% {Style.RESET_ALL}") 

def get_player_data() -> dict[str, str]:
    player_data: dict[str, str] = {}

    ## Check if file exists.
    if os.path.isfile("player.json"):
        pass
    else:
        generate_player_data()
    
    #now that we know it exists, load it.
    try: 
        player_data_file = open("player.json", "r")
    except OSError:
        print("Player file could not be opened")
    else:
        player_data = json.load(player_data_file)
        print("player data loaded")
        return player_data
    
def get_pattern_data() -> dict[str, int]:
    pattern_data: dict[str, int]

    ##Check if file exists.
    if os.path.isfile("patterns.json"):
        pass
    else:
        exit("Missing patterns.json")
    
    patterns_file = open("patterns.json", "r")
    patterns_data = json.load(patterns_file)
    print(patterns_data)

def slot_result() -> str:
    symbols_data: dict[str, int]

    ##Check if file exists.
    if os.path.isfile("symbols.json"):
        pass
    else:
        exit("Missing symbols.json")

    symbol_file = open("symbols.json", "r")
    symbol_data = json.load(symbol_file)
    print(symbol_data)

    symbol_index: int = r.randrange(0, len(symbol_data), 1)
    print(symbol_index)

    keys = list(symbol_data.keys())
    symbol: str = keys[symbol_index]

    return symbol









player_data: dict[str, str] = get_player_data()


###### GAME STATES ######
game_state: str      = "menu"
last_game_state: str = game_state
## menu
## pulling
## result

PULL_KEYBIND: int = ord("R")
PULL_KEYBIND_TEXT: str = chr(PULL_KEYBIND)

MENU_KEYBIND: int = ord("E")
MENU_KEYBIND_TEXT: str = chr(MENU_KEYBIND)

EXIT_KEYBIND: int = ord("V")
EXIT_KEYBIND_TEXT: str = chr(EXIT_KEYBIND)

pull_timer: int = 0

temp_money: int = 0
test: str = player_data["money"]
money: int = int(test)

print_ui()


while True: ##### Main Loop
    if game_state != last_game_state:
        print_ui()

    user_input: str = ""
    match game_state:
        case "menu":
            print_ui()
            user_input: str = input().capitalize()
            if (user_input == PULL_KEYBIND_TEXT):
                game_state = "pulling"
        case "pulling":
            print_ui()
            print(f"Pulling! {str(pull_timer)}")
            pull_timer += 1
            time.sleep(0.333)
            if pull_timer == 9:
                game_state = "result"
                pull_timer = 0
                temp_money = r.randrange(-50, 50)
        case "result":
            print_ui()
            money += temp_money
            temp_money = 0
            save_player_data()
            print(f"Press {MENU_KEYBIND_TEXT} to go back to the menu or press {PULL_KEYBIND_TEXT} to pull again")
            user_input: str = input().capitalize()
            if (user_input == MENU_KEYBIND_TEXT):
                game_state = "menu"
            if (user_input == PULL_KEYBIND_TEXT):
                game_state = "pulling"
        case _:
            print("{Fore.RED} Error in match game_state, invalid game_state")
        



    if user_input == EXIT_KEYBIND_TEXT:
        save_player_data()
        cls()
        exit(0)

    last_game_state: str = game_state
