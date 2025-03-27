import lyricsgenius
import spotipy

SPOTIFY = spotipy.Spotify(
    client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials(client_id='6aefc95eb5a54ff08faf24a8947273ca',
                                                                       client_secret='d4a234e3502446aeb71ff52b0132e1ba'))

GENIUS = None
