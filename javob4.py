import asyncio
import logging
import requests
import sys

from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from bs4 import BeautifulSoup

BOT_TOKEN = "6407054173:AAGLVOeIDhxDCT606vluqU1wBu8S_v6yut4"
dp = Dispatcher(storage=MemoryStorage())


class Menu(StatesGroup):
    news = State()


def menu_buttons():
    new_post = KeyboardButton(text="News 📨")
    return ReplyKeyboardMarkup(keyboard=[[new_post]], resize_keyboard=True, one_time_keyboard=True)


@dp.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer("Res")
    await msg.answer(f"Hello - 👤 {msg.from_user.full_name}")
    print(f"👤 - {msg.from_user.full_name}")
    await msg.answer(f"Tugmalardan birini tanlang ⤵️", reply_markup=menu_buttons())
    await state.set_state(Menu.news)


@dp.message(Menu.news)
async def menu_handler(msg: Message, state: FSMContext):
    response = requests.get("https://www.fitnessblender.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    for i in soup.find_all("div", "title-card-group"):
        txt1 = i.find("h2", "category").text
        await msg.answer(txt1)
    for i in soup.find_all("div", "sumary-group"):
        txt1 = i.find("h1", "content-title").text
        await msg.answer(txt1)


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
