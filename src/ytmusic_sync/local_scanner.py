import os
from mutagen.easyid3 import EasyID3

from .config import INPUT_PATH


def scan_local_music():

    songs = []

    # case 1: folder
    if os.path.isdir(INPUT_PATH):

        for file in os.listdir(INPUT_PATH):

            if not file.endswith(".mp3"):
                continue

            path = os.path.join(INPUT_PATH, file)

            try:
                audio = EasyID3(path)

                title = audio["title"][0]
                artist = audio["artist"][0]

                songs.append(f"{title} - {artist}")

            except Exception:

                songs.append(file.replace(".mp3", ""))

    # case 2: text file
    elif os.path.isfile(INPUT_PATH):

        with open(INPUT_PATH, "r") as f:

            for line in f:
                line = line.strip()

                if line:
                    songs.append(line)

    else:

        raise FileNotFoundError(f"{INPUT_PATH} not found")

    return songs
