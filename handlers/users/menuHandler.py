import logging
from aiogram.types import Message, CallbackQuery
from aiogram.utils import callback_data

from keyboards.inline.productskeyboard import productsMenu, booksMenu
from keyboards.inline.productskeyboard import coursesMenu
from loader import dp


@dp.message_handler(text_contains="Mahsulot")
async def select_category(message: Message):
    await message.answer(" Mahsulotni tanlang", reply_markup=productsMenu)


@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.id=}")
    await call.message.delete()
    await call.message.answer("Kursni tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="books")
async def buy_books(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kitoblar", reply_markup=booksMenu)
    await call.answer(cache_time=60)

