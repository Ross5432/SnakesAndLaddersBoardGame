
# menu.py - Menu Module
# Responsible for displaying and implementing the menu options

from gamecat_manager import get_game_list, add_game_to_list, search_game_list, update_game_in_list, delete_game_from_list
from game import display_game, input_game, edit_game

def display_menu():
    print("1. Display Game Catalogue")
    print("2. Add Game")
    print("3. Search Game Catalogue")
    print("4. Update Game")
    print("5. Delete Game")
    print("6. Quit")


def option_1():
    games = get_game_list()

    if not games:
        print("No games in the catalogue.")
        return
    
    for game in games:
        display_game(game)


def option_2():
    new_game = input_game()
    add_game_to_list(new_game)
    print("Game added successfully.")

   
def option_3():
    search_term = input("Enter game name or keyword: ")
    results = search_game_list(search_term)

    if not results:
        print("No matching games found.")
        return
    
    for game in results:
        display_game(game)



def option_4():
    name = input("Enter name of game to update: ")

    game = search_game_list(name)

    if not game:
        print("Game not found.")
        return

    updated_game = edit_game(game[0])
    update_game_in_list(game[0], updated_game)

    print("Game updated successfully.")


def option_5():
    name = input("Enter name of game to delete: ")

    deleted = delete_game_from_list(name)

    if deleted:
        print("Game deleted.")
    else:
        print("Game not found.")