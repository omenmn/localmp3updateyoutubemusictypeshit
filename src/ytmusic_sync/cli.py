from pathlib import Path
from typing import Annotated

import typer

from .yt_fetcher import get_recent_songs
from .local_scanner import scan_local_music
from .comparator import find_missing
from .utils import print_missing
from .downloader import download_songs

app = typer.Typer()


@app.command()
def main(
    music: Annotated[Path | None, typer.Option("--music", help="Music folder")] = None,
    song_list: Annotated[Path | None, typer.Option("--list", help="Song list file")] = None,
    download: Annotated[bool, typer.Option("--download", help="Download missing songs")] = False,
):
    print(f"DEBUG: music={music}, song_list={song_list}")
    source = music or song_list

    if source is None:
        print("Provide either --music or --list")
        raise typer.Abort()

    print("Fetching YouTube Music history...")
    yt_songs = get_recent_songs()

    print("Scanning local songs...")
    local_songs = scan_local_music(str(source))

    missing = find_missing(yt_songs, local_songs)

    print_missing(missing)

    if download and missing:

        output_dir = music if music else Path("downloads")

        download_songs(missing, str(output_dir))


if __name__ == "__main__":
    app()
