from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import course_callback, books_callback

productsMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 kurslar", callback_data="courses"),
            InlineKeyboardButton(text="📚 kitoblar", callback_data="books"),
        ],
        [
            InlineKeyboardButton(text="🔗 Mohirdev sahifasiga o'tish",
                                 url="https://mohirdev.uz/courses/telegram/lesson/xabar-osti-tugmalari-inline-keyboards-1-qism/")
        ],
        [
            InlineKeyboardButton(text="🔎 Qidirish", switch_inline_query_current_chat=" ")
        ],
        [
            InlineKeyboardButton(text="📲 Ulashish", switch_inline_query="Bot ajoyib")
        ],
    ]
)

# Pastki klaviaturalar
coursesMenu = InlineKeyboardMarkup(row_width=1)
python = InlineKeyboardButton(text="🐍 Python dasturlash asoslari",
                              callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

telegram_bot = InlineKeyboardButton(text="🤖 Mukammal telegram bot",
                                    callback_data=course_callback.new(item_name="course=telegram"))
coursesMenu.insert(telegram_bot)

django = InlineKeyboardButton(text=" 🌍 Django Web dasturlash",
                              callback_data=course_callback.new(item_name="django"))
coursesMenu.insert(django)

algorithm = InlineKeyboardButton(text="📡 Ma'lumotlar tuzilmasi va Algoritmlar",
                                 callback_data="courses:algortihm")
coursesMenu.insert(algorithm)

back_button = InlineKeyboardButton(text="⬅️ Ortga", callback_data='cancel')
coursesMenu.insert(back_button)

# Bir nechta tugmalar yaratish

books = {
    "Python dasturlash asoslari": "python_book",
    "C++ dastulash tili": "cpp_book",
    "Mukammal Dasturlash JavaScript": "js_book"
}

booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=books_callback.new(item_name=value)))
booksMenu.insert(back_button)
