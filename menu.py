
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
    # ================= STUDENT TASK START =================
    # Get the list of games from get_game_list()
    # and display each one using display_game().
    print()             # This statement can be replaced
    # ================== STUDENT TASK END ==================

def option_2():
    # ================= STUDENT TASK START =================
    # Ask the user for a new game using input_game()
    # then add it to the list using add_game_to_list().
    print()             # This statement can be replaced
    # ================== STUDENT TASK END ==================

def option_3():
    # ================= STUDENT TASK START =================
    # Ask the user what they want to search for,
    # call search_game_list(),
    # then display the matching game(s).
    print()             # This statement can be replaced
    # ================== STUDENT TASK END ==================

def option_4():
    # ================= STUDENT TASK START =================
    # Ask the user which game should be updated.
    # Find the game, call edit_game(...) to build the new record,
    # then call update_game_in_list(...).
    print()             # This statement can be replaced
    # ================== STUDENT TASK END ==================

def option_5():
    # ================= STUDENT TASK START =================
    # Ask the user which game should be deleted,
    # then call delete_game_from_list().
    print()             # This statement can be replaced
    # ================== STUDENT TASK END ==================
