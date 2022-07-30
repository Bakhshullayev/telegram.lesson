from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True),
            KeyboardButton(text="Location", request_location=True),
        ],
    ], resize_keyboard=True
)
