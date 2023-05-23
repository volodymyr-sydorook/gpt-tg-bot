from aiogram import Router
from aiogram.types import Message
from lexicon import LEXICON
from utils import check_sub_channel

router: Router = Router()


# This handler will respond to any user commands,
# not covered by the bot's logic
@router.message()
async def send_not_search_command(message: Message):
    if await check_sub_channel(message.from_user.id):
        await message.answer(LEXICON['command_non_existent'])
    else:
        await message.answer(LEXICON['not_sub_channel'])
