import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests

from config import TOKEN, weather_api

import random

bot = Bot(token=TOKEN) # https://t.me/aio_bot_my_bot
dp = Dispatcher()

@dp.message(Command('photo_url')) # если ввел команду /photo то
# отправим ему фотку или фотку из интернета
async def photo_url(message: Message):
    list = ["https://i.pinimg.com/736x/81/14/a1/8114a111992db0767789693670fe9756.jpg",
            "https://cdn1.ozone.ru/s3/multimedia-o/c600/6582603300.jpg",
            "https://yakutsk.evro-gift.ru/wa-data/public/shop/products/20/86/8620/images/33225/33225.970.jpg"
            ]
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption="Вот тебе фотка")

@dp.message(Command('weather'))
async def get_weather(message: Message):
    api_key = weather_api
    #url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp']
    await message.answer(f"Температура в Москве: {temp}°C")



@dp.message(Command('help')) # если получим команду /help
# то будет запускаться функция для которой прописан этот декоратор
async def help(message: Message):
    await message.answer("Тут будет помощь")

@dp.message(CommandStart()) # если получим команду /start
# то будет запускаться функция для которой прописан этот декоратор
async def start(message: Message):
    await message.answer("Привет")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())