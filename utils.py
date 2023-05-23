from config import bot, CHAT_ID, API_KEY
from lexicon import LEXICON
import pytesseract
from PIL import Image
import openai


async def check_sub_channel(user_id):
    """A function that returns True if the user is in the Telegram channel
    For the function to work, you need to make the bot the administrator of the Telegram channel"""
    try:
        chat_member = await bot.get_chat_member(chat_id=CHAT_ID, user_id=user_id)
        status_member = chat_member.status
        if status_member in ('member', 'creator'):
            return True
        return False
    except:
        pass


custom_config = r'--oem 3 --psm 6'


def text_recoqnition(file_path=''):
    """This function takes a photo_for_md path and returns a list with text from the photo_for_md
    Here is the website with the languages supported by these libraries https://www.jaided.ai/easyocr/"""
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img)
    return text


async def openai_message(msg_for_openai: str):
    openai.api_key = API_KEY
    name_model = "gpt-3.5-turbo"
    chat_history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": msg_for_openai}
    ]
    try:
        response = openai.ChatCompletion.create(model=name_model, messages=chat_history, max_tokens=4095)
        return response['choices'][0]['message']['content']
    except:
        return LEXICON['problem_message']
