from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator, ChannelParticipant
from telegram import *
from consts import *
import asyncio



async def check_membership(channel, user):
    try:
        participant = await CLIENT(GetParticipantRequest(channel, user))

        if isinstance(participant.participant, (ChannelParticipant, ChannelParticipantAdmin, ChannelParticipantCreator)):
            print('The user is a member of the channel.')
            return True
        else:
            print('The user is not a member of the channel.')
            return False

    except Exception as e:
        print(f'Error: {e}')
        return False


async def try_to_delete_message(chat_id, message_id):
    try:
        await asyncio.sleep(3)
        await CLIENT.delete_messages(chat_id, message_id)
    except Exception as e:
        pass