import asyncio
import logging

import other_handlers
import user_handlers
from config import bot, dp

# Initialize the logger
logger = logging.getLogger(__name__)


# Function for configuring and starting the bot
async def main():
    # Configuring the logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Output to the console information about the start of the bot
    logger.info('Starting bot')

    # Register routers in the dispatcher
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Skip the accumulated updates and run polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
