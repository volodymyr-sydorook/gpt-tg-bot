from aiogram import Bot, Dispatcher

dp: Dispatcher = Dispatcher()

BOT_TOKEN = '6032002243:A....'  # Replace with your own token from BotFather
API_KEY = 'sk-....'  # Replace the gpt3.5 turbo api key from the openai website with your own
CHAT_ID = '-10...  # Enter the chat ID that users must subscribe to before sending messages to the bot, the chat ID can be found in the bot https://t.me/username_to_id_bot by sending a link to your chat
TWS = 0.1  # Text animation writing speed, 0.1 high speed 0.9 slow

# Initialize bot and dispatcher
bot: Bot = Bot(token=BOT_TOKEN,
               parse_mode='HTML')

