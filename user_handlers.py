from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from lexicon import LEXICON
from utils import openai_message, text_recoqnition, check_sub_channel
from config import bot, TWS

import time
import asyncio
import os

router: Router = Router()


async def text_writing_animation(message, msg_for_user):
    """A function that displays an animation of writing text"""
    try:
        response = await message.answer(text='...')
        rest = ''
        for char in msg_for_user.split(' '):
            rest += ' ' + char
            await bot.edit_message_text(rest, chat_id=message.chat.id, message_id=response.message_id)
            await asyncio.sleep(TWS)
    except:
        pass


# Handler for processing /start and /help commands
@router.message(Command(commands=['start', 'help']))
async def help_start_command(message: Message):
    if await check_sub_channel(message.from_user.id):
        await message.answer(LEXICON['command_start_help'])
    else:
        await message.answer(LEXICON['not_sub_channel'])


# Handler for commands /reset
@router.message(Command(commands=['reset']))
async def reset_command(message: Message):
    if await check_sub_channel(message.from_user.id):
        await message.reply(LEXICON['command_reset'])
    else:
        await message.answer(LEXICON['not_sub_channel'])


# Handler for processing photos sent by the user
@router.message(F.photo)
async def photo_processing(message: Message):
    if await check_sub_channel(message.from_user.id):
        # upload a photo_for_md
        file_id = message.photo[-1].file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        name_photo = str(time.time())
        await bot.download_file(file_path, f'{name_photo}.png')

        # Reading text from a photo_for_md
        photo_text = str(text_recoqnition(f'{name_photo}.png'))

        # GPT responds to text taken from a photo_for_md
        msg_for_user = await openai_message(msg_for_openai=photo_text)

        # Animation of writing text
        await text_writing_animation(message, msg_for_user)

        # Delete a photo_for_md
        if os.path.exists(f'{name_photo}.png'):
            os.remove(f'{name_photo}.png')
    else:
        await message.answer(LEXICON['not_sub_channel'])


# This handler accepts all text messages
@router.message(F.text)
async def get_chat_gpt(message: Message):
    if await check_sub_channel(message.from_user.id):
        msg_for_user = await openai_message(msg_for_openai=message.text)

        # Animation of writing text
        await text_writing_animation(message, msg_for_user)
    else:
        await message.answer(LEXICON['not_sub_channel'])
