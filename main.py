from bs4 import BeautifulSoup
import requests
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "8e25b53f800c4cf7a666b9f6bd5f65ac"
client_secret = "bdb0e822b66e4955ac83c8770063ade0"

time = input("Enter time you wish to travel to in YYYY-MM-DD format:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{time}")
web_scrap = response.text

soup = BeautifulSoup(web_scrap, "lxml")
song_titles = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")

song_list = [song.getText().strip() for song in song_titles]

print(song_list[::-1])

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=Client_ID,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

