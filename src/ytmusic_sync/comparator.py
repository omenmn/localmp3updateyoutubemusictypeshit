from rapidfuzz import fuzz

from .config import FUZZY_THRESHOLD


def find_missing(online_songs, local_songs):

    missing = []

    for song in online_songs:

        found = False

        for local in local_songs:

            score = fuzz.ratio(song.lower(), local.lower())

            if score >= FUZZY_THRESHOLD:
                found = True
                break

        if not found:
            missing.append(song)

    return missing
