from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="How are you?")
        ],
        [
            KeyboardButton(text="How old are y?")
        ]
    ]
)