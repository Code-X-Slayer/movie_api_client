from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = "http://www.omdbapi.com/"
TIMEOUT = 10

payload = {
    't' : 'toy story',
    'apikey' : API_KEY
}

response = requests.get(URL, params=payload, timeout=TIMEOUT)
response.raise_for_status()
# print(response.status_code)
if response.status_code != 200:
    print('error')
# print(response.text)
data = response.json()
if 'response' in data and not data['response']:
    print('error')
print({
    "title": data["Title"],
    "year": data["Year"],
    "director": data["Director"],
    "genre": data["Genre"],
    "actors": data["Actors"],
    "rating": data["imdbRating"],
    "runtime": data["Runtime"],
    "plot": data["Plot"],
})

{
    'title': 'Titanic',
    'year': '1997',
    'director': 'James Cameron',
    'genre': 'Drama, Romance',
    'actors': 'Leonardo DiCaprio, Kate Winslet, Billy Zane',
    'rating':'8.0',
    'runtime': '194 min',
    'plot': 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious,ill-fated R.M.S. Titanic.'
}

{
    'title': 'Toy Story',
    'year': '1995',
    'director': 'John Lasseter',
    'genre': 'Animation, Adventure, Comedy',
    'actors': 'Tom Hanks, Tim Allen, Don Rickles',
    'rating': '8.3',
    'runtime': '81 min',
    'plot': "A cowboy doll is profoundly jealous when a new spaceman action figure supplants him as the top toy in a boy's bedroom. When circumstances separate them from their owner, the duo have to put aside their differences to return to him."
}