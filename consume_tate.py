import requests
from pprint import pprint


ARTIST_URL = "http://127.0.0.1:8000/api/artists"
ARTWORK_URL = "http://127.0.0.1:8000/api/artworks/"

params = {
    'name': 'gogh',
}
response = requests.get(ARTIST_URL, params=params)

pprint(response.json())

response = requests.get(ARTWORK_URL, params={
    'title': 'sheep'
})

print('-' * 60)
pprint(response.json())
print('-' * 60)
data = response.json()
for artwork in data:
    artist_data = requests.get(artwork['artist']).json()
    print(artist_data)
    print(f"{artwork['title']} by {artist_data['name']}")
    break

new_artist = {
    'name': 'Abernathy, Colleen',
    'place_of_birth': 'Berkeley, CA',
    'birth_year': 1956,
    'death_year': None,
    'tate_url': None,
    'artworks': None,
}

response = requests.post(ARTIST_URL, data=new_artist)
print(response.status_code)

