
# game.py - Game Module
# Responsible for creating and updating a game record


def create_game(title, genre, year, publisher, min_players, max_players, play_time_mins, cooperative, rating):
    return {
        "title": title,
        "genre": genre,
        "year": year,
        "publisher": publisher,
        "min_players": min_players,
        "max_players": max_players,
        "play_time_mins": play_time_mins,
        "cooperative": cooperative,
        "rating": rating
    }
    
  
def get_name(game):
    return game["title"]


def display_game(game):
    print("\n--- Game ---")
    print("Title:", game["title"])
    print("Genre:", game["genre"])
    print("Year:", game["year"])
    print("Publisher:", game["publisher"])
    print("Players:", game["min_players"], "-", game["max_players"])
    print("Play Time:", game["play_time_mins"], "mins")
    print("Cooperative:", game["cooperative"])
    print("Rating:", game["rating"])


def input_game():
    title = input("Title: ")
    genre = input("Genre: ")
    year = int(input("Year: "))
    publisher = input("Publisher: ")
    min_players = int(input("Min players: "))
    max_players = int(input("Max players: "))
    play_time_mins = int(input("Play time (mins): "))
    cooperative = input("Cooperative (y/n): ").lower() == "y"
    rating = float(input("Rating (0-10): "))

    return create_game(
        title, genre, year, publisher,
        min_players, max_players,
        play_time_mins, cooperative, rating
    )

def edit_game(existing_game):
    print("Press Enter to keep current value.\n")

    title = input(f"Title ({existing_game['title']}): ") or existing_game["title"]
    genre = input(f"Genre ({existing_game['genre']}): ") or existing_game["genre"]
    year = input(f"Year ({existing_game['year']}): ") or existing_game["year"]
    publisher = input(f"Publisher ({existing_game['publisher']}): ") or existing_game["publisher"]
    min_players = input(f"Min players ({existing_game['min_players']}): ") or existing_game["min_players"]
    max_players = input(f"Max players ({existing_game['max_players']}): ") or existing_game["max_players"]
    play_time_mins = input(f"Play time ({existing_game['play_time_mins']}): ") or existing_game["play_time_mins"]
    cooperative = input(f"Cooperative ({existing_game['cooperative']}): ") or existing_game["cooperative"]
    rating = input(f"Rating ({existing_game['rating']}): ") or existing_game["rating"]

    return create_game(
        title,
        genre,
        int(year),
        publisher,
        int(min_players),
        int(max_players),
        int(play_time_mins),
        cooperative.lower() == "y" if isinstance(cooperative, str) else cooperative,
        float(rating)
    )

