from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.pythonkeyboard import menu_python

from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)


@dp.message_handler(text="Telegram bot")
async def send_link(message: Message):
    await message.answer("Telegram bot kursimiz :https://github.com/danielgatis/rembg")


@dp.message_handler(text="Python")
async def send_python(message: Message):
    await message.answer("Mavzuni tanlang", reply_markup=menu_python)


@dp.message_handler(text="Python")
async def send_python(message: Message):
    await message.answer("Mavzuni tanlang", reply_markup=menu_python)


@dp.message_handler(text="Kirish")
async def send_python(message: Message):
    await message.answer("https://github.com/Bakhshullayev/python.lesson", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Boshiga")
async def send_python(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)
