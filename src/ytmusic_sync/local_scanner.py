import os
from mutagen.easyid3 import EasyID3


def scan_local_music(path):

    print(path)

    songs = []

    # folder mode
    if os.path.isdir(path):

        for file in os.listdir(path):

            if not file.endswith(".mp3"):
                continue

            full_path = os.path.join(path, file)

            try:
                audio = EasyID3(full_path)

                title = audio["title"][0]
                artist = audio["artist"][0]

                songs.append(f"{title} - {artist}")

            except Exception:

                songs.append(file.replace(".mp3", ""))

    # text file mode
    elif os.path.isfile(path):

        with open(path) as f:

            for line in f:
                line = line.strip()

                if line:
                    songs.append(line)

    else:

        raise FileNotFoundError(f"{path} not found")

    return songs
