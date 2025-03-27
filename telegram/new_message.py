from telethon import events, client , Button
from consts import *
from spotify.album import Album
from spotify.artist import Artist
from spotify.playlist import Playlist
from spotify.song import Song
from telegram import CLIENT
from telegram.utils import handle_search_message
from dataBase import *
from functions import *
from spotify.utils import *


@CLIENT.on(events.NewMessage(pattern="/start ?(.*)"))
async def start(event):
    ref_code = event.pattern_match.group(1)
    user_id = event.sender_id

    buttons = [
        [Button.text("📢 my status" , resize=True)],
    ]
    if ref_code:
        result = add_referral(user_id, ref_code)
        if result:
            await event.respond(WELCOME_MESSAGE , buttons= buttons, link_preview=False)
    else:
        if await is_user_exist(user_id):
            await event.respond(WELCOME_MESSAGE, buttons=buttons , link_preview=False)
        else:
            user_info =await add_user(user_id)
            await event.respond(WELCOME_MESSAGE , buttons=buttons , link_preview=False)


async def handle_track(event: events.NewMessage.Event, msg_link):
    print(f'[TELEGRAM] song callback query: {msg_link}')
    message = await Song(msg_link).song_telethon_template()
    await event.respond(message[0], thumb=message[1], buttons=message[2])


async def handle_album(event: events.NewMessage.Event, msg_link , message_ok , user_id):
    print(f'[TELEGRAM] album callback query: {msg_link}')
    message = await Album(msg_link).album_telegram_template()
    if message[3] > 1000:
        await try_to_delete_message(user_id ,message_ok.id)
        await event.respond(more_than_1000_tracks_message)
        return

    await event.respond(message[0], thumb=message[1], buttons=message[2])


async def handle_artist(event: events.NewMessage.Event, msg_link):
    print(f'[TELEGRAM] artist callback query: {msg_link}')
    message = await Artist(msg_link).artist_telethon_template()
    await event.respond(message[0], buttons=message[1])


async def handle_playlist(event: events.NewMessage.Event, msg_link , message_ok , user_id):
    print(f'[TELEGRAM] playlist callback query: {msg_link}')
    message = await Playlist(msg_link).playlist_template()
    if message[2] > 1000:
        await try_to_delete_message(user_id ,message_ok.id)
        await event.respond(more_than_1000_tracks_message)
        return
    await event.respond(message[0], buttons=message[1])







@CLIENT.on(events.NewMessage(pattern="/referral"))
async def referral(event):
    user_id = event.sender_id
    referral_link = get_referral_link(user_id)
    await event.respond(referral_link)




@CLIENT.on(events.NewMessage(pattern="📢 my status"))
async def status_handler(event):
    user_id = event.sender_id
    user_info = await get_user(user_id)
    referral_count = await get_referral_count(user_id)
    ###
    plan= 'A'
    ###
    button = [
        [Button.inline('referral link' ,data='referral_link'),
        Button.inline('by plan' ,data='plan')]
    ]
    USER_INFO = USER_INFO_MESSAGE.format(user_id=user_id ,referral_count=referral_count ,plan=plan)
    await event.respond(USER_INFO ,buttons=button)


@CLIENT.on(events.CallbackQuery(pattern=b"referral_link"))
async def referral_link(event):
    user_id = event.sender_id
    referral_link = await get_referral_link(int(user_id))
    referral_link_message = GET_REFERRAL_LINK_MESSAGE.format(referral_link=referral_link)
    button = [
        [
            Button.inline('by plan', data='plan')
        ]
    ]
    await event.respond(referral_link_message , buttons=button)

@CLIENT.on(events.CallbackQuery(pattern=b"plan"))
async def plan(event):
    user_id = event.sender_id
    await event.respond(PLANS_MESSAGE)


@CLIENT.on(events.NewMessage)
async def download(event: events.NewMessage.Event):
    # message is private
    if event.is_private and not event.raw_text.startswith('/start'):
        user_id = event.sender_id

        message_ok = CLIENT.send_message(user_id , CONFIRM_MESSAGE)

        # Check the membership status and stop continuing if user is not a member
        if check_membership(CHANNEL , user_id):
            pass
        else:
            keyboard = [[Button.url("Join", PROMOTE_CHANNEL_LINK)]]

            message = await CLIENT.send_message(
                user_id,
                NOT_SUBSCRIBED_TO_CHANNEL_MESSAGE,
                buttons=keyboard,
                parse_mode="Markdown",
                link_preview=False
            )

            await try_to_delete_message(user_id, message_ok.id)

        valid_spotify_links_in_user_text = get_valid_spotify_links(event.text)

        # if user sends multiple links combined with normal text we only extract and
        # analyze first one so the bot won't be spammed
        first_link = valid_spotify_links_in_user_text[0]

        if get_link_type(first_link) == "shortened":
            # log(bot_name + " log:\n🔗🩳 shortened link sent from user: " + str(message.chat.id))
            first_link = get_redirect_link(first_link)

        link_type = get_link_type(first_link)
        if link_type not in ["track", "album", "playlist"]:
            await try_to_delete_message(user_id, message_ok.id)
            CLIENT.send_message(user_id, "Looks like this link is wrong, expired or not supported. Try another.")
            # log(bot_name + " log:\n🛑 error in handling short link.")
            return


        msg = first_link

        print(f'[TELEGRAM] New message: {msg}')
        msg_link = text_finder(msg)
        if msg_link.startswith('https://open.spotify.com/'):
            # Process different types of Spotify links
            user_id = event.sender_id
            if 'album' in msg_link:
                await handle_album(event, msg_link , message_ok , user_id)
            elif 'track' in msg_link:
                await handle_track(event, msg_link)
            elif 'playlist' in msg_link:
                await handle_playlist(event, msg_link , message_ok , user_id)
            elif 'artist' in msg_link:
                await handle_artist(event, msg_link)
            else:
                await handle_search_message(event)
        else:
            await handle_search_message(event)


def text_finder(txt):
    index = txt.find("https://open.spotify.com")
    if index != -1:
        return txt[index:]
    return ''
