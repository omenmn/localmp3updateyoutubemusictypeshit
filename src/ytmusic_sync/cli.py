from .yt_fetcher import get_recent_songs
from .local_scanner import scan_local_music
from .comparator import find_missing
from .utils import print_missing


def main():

    print("Fetching YouTube Music history...")
    yt_songs = get_recent_songs()

    print("Scanning local library...")
    local_songs = scan_local_music()

    missing = find_missing(yt_songs, local_songs)

    print_missing(missing)
