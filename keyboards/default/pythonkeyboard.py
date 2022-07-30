from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPyhon = ReplyKeyboardMarkup(
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
    resize_keyboard=True
)
