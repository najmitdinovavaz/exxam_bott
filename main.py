import asyncio
import logging
import sys

import httpx
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from bs4 import BeautifulSoup

from buttons import number_button, start_button, men_or_women_button, training

TOKEN = "6407054173:AAGLVOeIDhxDCT606vluqU1wBu8S_v6yut4"

dp = Dispatcher()


class Menu(StatesGroup):
    menu = State()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Assalomu alaykum ! Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi",
                         reply_markup=number_button())


@dp.message(lambda message: message.text == "NewPost")
async def new_handler(message: Message):
    await message.answer("https://www.fitnessblender.com/")


@dp.message(Command)
async def new_handler(message: Message, state: FSMContext):
    if message.text == "NewPost":
        await message.answer("⏳")
        response = httpx.get("https://www.fitnessblender.com/")
        soup = BeautifulSoup(response.content, 'html.parser')
        for i in soup.find_all("div", "summary-group"):
            await message.answer(f"{i.find_all('h1', 'content-title').text}")
        await message.answer(f"Choose one of the buttons ⤵")
        await state.set_state(Menu.menu)


@dp.message(lambda message: message.text == "Filial 📍")
async def loc_handler(message: Message):
    await message.answer_location(41.30465070299682, 69.25317846453066, reply_markup=number_button())


@dp.message(lambda message: message.text == "Start ✅")
async def starts_handler(message: Message):
    await message.answer(f"Quydagilardan birontasini tanlang 👇", reply_markup=start_button())


@dp.message(lambda message: message.text == "Men 🧍‍♂️" or "Woman 🧍‍♀️")
async def men_handler(message: Message):
    await message.answer(f"Quydagilarni birontasini tanlang 👇", reply_markup=men_or_women_button())


@dp.message(lambda message: message.text == "1 - oy")
async def training_handler(message: Message):
    await message.answer(f"Quydagilarni birontasini tanlang 👇", reply_markup=training())


@dp.message(lambda message: message.text == "3 - oy" or "4 - oy")
async def train_handler(message: Message):
    await message.answer(f"Quydagilarni birontasini tanlang 👇", reply_markup=training())


@dp.message(lambda message: message.text == "NewPost")
async def new_handler(message: Message, state: FSMContext):
    response = httpx.get("https://www.fitnessblender.com/")
    soup = BeautifulSoup(response.content, 'html.parser')
    for i in soup.find_all("div", "summary-group"):
        await message.answer(f"{i.find_all('h1', 'content-title').text}")
    await message.answer(f"Choose one of the buttons ⤵", reply_markup=number_button())
    await state.set_state(Menu.menu)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
