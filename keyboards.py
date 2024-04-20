from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/kitty')],
    ],
    resize_keyboard=True,
)
