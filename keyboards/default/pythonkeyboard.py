from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_python = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kirish"),
            KeyboardButton(text="Kerakli dasturlar"),
            KeyboardButton(text="Hello World"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga")

        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
