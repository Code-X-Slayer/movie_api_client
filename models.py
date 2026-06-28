"""
models.py

Holds the data structure for a movie object.
"""

from dataclasses import dataclass

@dataclass
class Movie:
    """Defines the exact data types we expect for a movie"""
    title: str
    year: int
    director: str
    genre: list[str]
    actors: list[str]
    rating: float
    runtime: int
    plot: str

