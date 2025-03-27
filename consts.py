
WELCOME_MESSAGE = '''Hi😃👋
Send me a link from spotify and I'll download it for you.

some example links 👇

♪ track (very fast download)
https://open.spotify.com/track/734dz1YaFITwawPpM25fSt

🎵 album (fast download)
https://open.spotify.com/album/0Lg1uZvI312TPqxNWShFXL

🎶 playlist (normal download)
https://open.spotify.com/playlist/37i9dQZF1DWX4UlFW6EJPs
'''


CONFIRM_MESSAGE = "Ok🙂👍\nPlease be patient and wait till I download all of your link.\n\nYou will get a message in the end."


NOT_SUBSCRIBED_TO_CHANNEL_MESSAGE = '''Your link is correct✅.
Join to get access to database, then send your link again.'''

USER_INFO_MESSAGE = """
user : {user_id}
referral count : {referral_count}
plan : {plan}
"""

GET_REFERRAL_LINK_MESSAGE = """
your referral link is : 
{referral_link}
you can also get a plan
"""

PLANS_MESSAGE = """
PLAN A : 50$
PLAN B : 30$
PLAN C : 20$
"""




ARTISTS_MESSAGE = '''Please send the name of the artist like this: Artist Name'''


SINGLE_MESSAGE = '''Please send the name of the song like this:
Song Name
or for better search, use this format:
Song Name - Artist Name'''

ALBUM_MESSAGE = '''Please send the name of the album like this:
Album Name
or for better search, use this format:
Album Name - Artist Name'''

NOT_FOUND_STICKER = 'CAACAgQAAxkBAAIFSWBF_m3GHUtZJxQzobvD_iWxYVClAAJuAgACh4hSOhXuVi2-7-xQHgQ'

NOT_IN_DB = '❌💾 Song is not in database, this might take longer'

DOWNLOADING = 'downloading...'

UPLOADING = 'uploading...'

PROCESSING = 'processing...'

ALREADY_IN_DB = '💾already in database'

NO_LYRICS_FOUND = '❌No lyrics found'

SONG_NOT_FOUND = '❌Song Not Found'

ALBUM_HAS_SENT_SUCCESSFULLY = '🎧album sent!'

PLAYLIST_HAS_SENT_SUCCESSFULLY = '🎧playlist first 50 songs has sent!'



spotify_shortened_link_pattern = r'https?:\/\/spotify\.link\/[A-Za-z0-9]+'
spotify_track_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?track\/[a-zA-Z0-9]+'
spotify_album_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?album\/[a-zA-Z0-9]+'
spotify_playlist_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?playlist\/[a-zA-Z0-9]+'
spotify_correct_link_pattern = spotify_track_link_pattern + "|" + spotify_album_link_pattern + "|" + spotify_playlist_link_pattern + "|" + spotify_shortened_link_pattern
deezer_link_pattern = r'https?:\/\/(?:www\.)?deezer\.com\/(?:\w{2}\/)?(?:\w+\/)?(?:track|album|artist|playlist)\/\d+'
soundcloud_link_pattern = r"(?:https?://)?(?:www\.)?soundcloud\.com/([a-zA-Z0-9-_]+)/([a-zA-Z0-9-_]+)"
youtube_link_pattern = r"(?:(?:https?:)?//)?(?:www\.)?(?:(?:youtube\.com/(?:watch\?.*v=|embed/|v/)|youtu.be/))([\w-]{11})"
spotify_episode_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?episode\/[a-zA-Z0-9]+'
spotify_artist_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?artist\/[a-zA-Z0-9]+'
spotify_user_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?user\/[a-zA-Z0-9]+'


more_than_1000_tracks_message = "Bot can't download playlists more than 1000 tracks at the moment.\
This feature will be added later."