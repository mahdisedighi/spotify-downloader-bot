from spotify import SPOTIFY
from spotify.song import Song
from consts import *
import re
import requests


def get_redirect_link(shortened_link):
    response = requests.head(shortened_link, allow_redirects=True)
    return response.url


def get_link_type(text):
    if re.match(spotify_track_link_pattern, text):
        return "track"
    elif re.match(spotify_album_link_pattern, text):
        return "album"
    elif re.match(spotify_playlist_link_pattern, text):
        return "playlist"
    elif re.match(spotify_shortened_link_pattern, text):
        return "shortened"
    else:
        return False

def get_valid_spotify_links(text):
    regexes = [spotify_shortened_link_pattern, spotify_track_link_pattern, spotify_album_link_pattern, spotify_playlist_link_pattern]
    # Create a compiled regular expression object
    # by joining the regex patterns with the OR operator |
    regex_combined = re.compile("|".join(regexes))
    # Find all matches and store them in a list
    all_matches = [match.group() for match in regex_combined.finditer(text)]
    print(all_matches) # as debug
    return all_matches


def album(link):
    results = SPOTIFY.album_tracks(link)
    albums = results['items']
    while results['next']:
        results = SPOTIFY.next(results)
        albums.extend(results['items'])
    return albums


def artist(link):
    results = SPOTIFY.artist_top_tracks(link)
    albums = results['tracks']
    return albums


def search_album(track):
    results = SPOTIFY.search(track)
    return results['tracks']['items'][0]['album']['external_urls']['spotify']


def playlist(link):
    results = SPOTIFY.playlist_items(link)
    return results['items'][:50]


def search_single(q) -> list[Song]:
    results = SPOTIFY.search(q)
    songs_list = []
    for item in results['tracks']['items']:
        songs_list.append(Song(item['id']))
    return songs_list


def search_artist(artist):
    results = SPOTIFY.search(artist)
    return results['tracks']['items'][0]['artists'][0]["external_urls"]['spotify']
