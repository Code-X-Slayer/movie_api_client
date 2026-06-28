"""
main.py

The main entry point that runs the program loop and links everything together.
"""

import input_handler as ip
from models import Movie
from api_client import fetch_movie, print_movie

def print_menu() -> None:
    """Displays the simple text menu to the user."""
    print("\n====Movie API Menu====")
    print("1. Search Movie")
    print("2. Exit")

def search_movie_handler() -> None:
    """Asks for a title, fetches the data, and prints it if successful."""
    title = ip.read_string("Enter movie title to search: ")
    movie: Movie | None = fetch_movie(title)
    if movie:
        print_movie(movie)

def main() -> None:
    """Keeps the application running in a loop until the user chooses to exit."""
    while True:
        print_menu()
        choice = ip.read_char("Enter choice: ")
        if choice=='1':
            search_movie_handler()
        elif choice=='2':
            print('Exiting ...')
            break
        else:
            print("Invalid choice! Try Again")

if __name__ == '__main__':
    main()