import asyncio
from aiogram import Bot, Dispatcher
from handlers import (
    bot_commands,
    bot_messages,
    bot_errors,
    bot_startup)


async def main() -> None:
    bot = Bot('')
    dp = Dispatcher()
    dp.include_routers(
        bot_commands.router,
        bot_messages.router,
        bot_startup.router,
        bot_errors.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
