from ytmusicapi import YTMusic
from .config import HEADERS_FILE

def get_recent_songs():

    yt = YTMusic(HEADERS_FILE)

    history = yt.get_history()

    songs = []

    for item in history:

        title = item.get("title")

        artists = item.get("artists")

        if not title or not artists:
            continue

        artist = artists[0]["name"]

        songs.append(f"{title} - {artist}")

    return songs
