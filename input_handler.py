"""
input_handler.py

Handles all terminal interactions and converts raw dictionary data into a Movie object.
"""

from models import Movie

def read_string(msg: str) -> str:
    """Prompts the user for a non-empty string and returns it in lowercase."""
    while True:
        s = input(msg).strip().lower()
        if not s:
            print("Error: Input can't be empty")
            continue
        return s

def read_char(msg: str) -> str:
    """Prompts the user for a single-character string."""
    while True:
        s = read_string(msg)
        if len(s) != 1:
            print("Error: Input must consists only one char")
            continue
        return s

def read_movie(movie: dict) -> Movie:
    """Extracts data from the raw dictionary and casts it into our strictly typed Movie object."""
    return Movie(
        title=movie['title'],
        year=int(movie['year']),
        director=movie['director'],
        genre=movie['genre'].split(', '),
        actors=movie['actors'].split(', '),
        rating=float(movie['rating']),
        runtime=int(movie['runtime'].split(' ')[0]),
        plot=movie['plot']
    )

