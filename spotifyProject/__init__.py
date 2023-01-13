from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "ab50c61b63e94e49b82894b153cb8dc2"
CLIENT_SECRET = "c54afb1ad6d04b3a8431c8f3bbcafabb"
REDIRECT_URI = "http://example.com"  # "https://localhost:8080/callback"
SCOPE = "playlist-modify-private"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
print(date)

response = requests.get(URL + date)
billboard_page = response.text

pp = pprint.PrettyPrinter(indent=2)

soup = BeautifulSoup(billboard_page, "html.parser")

# Getting all the songs titles
songs_info = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
songs_titles = [title.get_text().strip() for title in songs_info]

# Login Spotify
sp_auth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE,
                       show_dialog=True, cache_path="toke.txt")
sp = spotipy.Spotify(auth_manager=sp_auth)

# Create a new playlist
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Add all the songs to the playlist
year = date.split("-")[0]
for title in songs_titles:
    song_info = sp.search(q=f"track:{title} year:{year}" , limit=1)
    try:
        song_id = song_info['tracks']['items'][0]['id']
        sp.playlist_add_items(playlist_id=playlist['id'], items=[song_id])
    except IndexError:
        print(f"{title} doesn't exist in Spotify")

# sp.playlist_add_items(playlist_id=playlist['id'], items=playlist_songs)

