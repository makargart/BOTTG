import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("8140610350:AAGdgBH0tSe4Wb_7VBb8f_y6vcfVu6jeT_s")  # токен берём из переменных окружения
ADMIN_ID = int(os.getenv("@MakarGart"))  # твой телеграм ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    await message.forward(ADMIN_ID)
    await message.reply("Фото отправлено админу!")

@dp.message_handler(content_types=['text'])
async def handle_text(message: types.Message):
    await bot.send_message(ADMIN_ID, f"Комментарий от @{message.from_user.username}:\n{message.text}")
    await message.reply("Комментарий передан админу!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


