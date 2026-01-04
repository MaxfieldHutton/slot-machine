import random as r
from colorama import Fore
import os
import time
import json
import datetime as dt

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
        print(f"Press {str(PULL_KEYBIND_TEXT)} to spin")
    elif game_state == "pulling":
        print("Game state pulling")
    elif game_state == "result":
        print("Game state result")
    else:
        print(f"{Fore.RED} Error in print_ui function, invalid game_state")


def generate_player_data() -> None:
    default_data: dict[str, str] = {"money":"50","last login":f"{dt.datetime.now()}"}
    with open("player.json", "w") as file:
        json.dump(default_data, file, indent=4)
    print("created player file")    

def get_player_data() -> dict:

    ##Check if file exists.
    file_exists: bool = False
    if os.path.isfile("player.json"):
        file_exists = True
    else:
        generate_player_data()
    
    #now that we know it exists, load it.
    try: 
        player_data_file = open("player.json", "r")
    except OSError:
        print("Player file could not be opened")
    else:
        print("sometrhging")




player_data: dict = get_player_data()
input()


###### GAME STATES ######
game_state: str      = "menu"
last_game_state: str = game_state
## menu
## pulling
## result

PULL_KEYBIND: int = ord("R")
PULL_KEYBIND_TEXT: str = chr(PULL_KEYBIND)

player_data = []

pull_timer = 0


print_ui()


while True: ##### Main Loop
    if game_state != last_game_state:
        print_ui()

    user_input: str = ""
    match game_state:
        case "menu":
            user_input: str = input().capitalize()
            if (user_input == "R"):
                game_state = "pulling"
        case "pulling":
            print(f"Pulling! {str(pull_timer)}")
            pull_timer += 1
            time.sleep(0.333)
            if pull_timer == 9:
                game_state = "result"
        case "result":
            print("result screen")
            user_input: str = input().capitalize()
        case _:
            print("{Fore.RED} Error in match game_state, invalid game_state")
        



    if user_input == "E":
        exit(0)

    last_game_state: str = game_state
