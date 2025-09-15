from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import os

TOKEN = os.getenv("BOT_TOKEN")  # токен берём из переменных окружения
ADMIN_ID = int(os.getenv("ADMIN_ID"))  # твой телеграм ID

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



