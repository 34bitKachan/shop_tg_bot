from aiogram import Bot, Dispatcher
from aiogram.filters.command import CommandStart
from aiogram.types import Message

import asyncio

token = "7934857363:AAHwwYf-oSN2j1Igjl9IazVabnBCz4hJi0U"
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart)
async def hello_bot(mes: Message):
    await mes.answer("Hello World!")

async def start_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_bot())
