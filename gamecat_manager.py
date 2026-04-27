
# gamecat_manager.py - Game Catalogue Manager Module
# Responsible for maintaining and modifying the game catalogue list

gamecat_list = []

def add_game_to_list(game):
    gamecat_list.append(game)


def get_game_list():
    return gamecat_list


def search_game_list(query):
    results = []

    for game in gamecat_list:
        if query.lower() in game["title"].lower():
            results.append(game)

    return results


def update_game_in_list(original_title, updated_game):
    for i in range(len(gamecat_list)):
        if gamecat_list[i]["title"].lower() == original_title.lower():
            gamecat_list[i] = updated_game
            return True

    return False


def delete_game_from_list(game):
     if game in gamecat_list:
        gamecat_list.remove(game)
        return True

    return False


