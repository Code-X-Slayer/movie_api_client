"""
api_client.py

Abstracts all the networking logic to talk to the OMDB API.
"""

from models import Movie
import input_handler as ip

from dotenv import load_dotenv
import os
import requests

# Load environment variables from the .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = "http://www.omdbapi.com/"
TIMEOUT = 10

# Fail-fast check: crash the app immediately if the API key is missing
if not API_KEY:
    raise ValueError("API_KEY is missing! Please check your env file.")  

def fetch_movie(title: str) -> Movie | None:
    """Prepares the API request with the title and API key"""
    payload = {'t' : title, 'apikey' : API_KEY}

    try:
        response = requests.get(URL, params=payload, timeout=TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: Network issue or API failure - {e}")
        return None
    
    data = response.json()

    if data.get('Response') == 'False':
        print(f"Error: Movie with title '{title}' not found")
        return None

    return ip.read_movie({
        "title": data.get("Title", "N/A"),
        "year": data.get("Year", "N/A"),
        "director": data.get("Director", "N/A"),
        "genre": data.get("Genre", "N/A"),
        "actors": data.get("Actors", "N/A"),
        "rating": data.get("imdbRating", "N/A"),
        "runtime": data.get("Runtime", "N/A"),
        "plot": data.get("Plot", "N/A"),
    })

def print_movie(movie: Movie) -> None:
    """Prints the structured movie data neatly to the console."""
    print("\nMovie Details")
    print("==================================")
    print(f"Title       : {movie.title}")
    print(f"Year        : {movie.year}")
    print(f"Director    : {movie.director}")
    print(f"Genre       : {movie.genre}")
    print(f"Actors      : {movie.actors}")
    print(f"IMDb Rating : {movie.rating}")
    print(f"Runtime     : {movie.runtime}")
    print(f"Plot        : {movie.plot}")
    print("==================================")

