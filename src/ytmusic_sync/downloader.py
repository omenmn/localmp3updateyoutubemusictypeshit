import subprocess
from pathlib import Path


def download_songs(songs, output_dir):

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for song in songs:

        print(f"Downloading: {song}")

        cmd = [
            "yt-dlp",
            f"ytsearch1:{song}",
            "-x",
            "--audio-format",
            "mp3",
            "-o",
            f"{output_dir}/%(title)s.%(ext)s",
        ]

        subprocess.run(cmd)
