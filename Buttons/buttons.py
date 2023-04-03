from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Повтор 🔄'),
    KeyboardButton(text='Новый чат ⏩'))

keyboard_yes_no = InlineKeyboardMarkup().add(
        InlineKeyboardButton('Новый чат', callback_data='yes'),
        InlineKeyboardButton('Остаться', callback_data='no'))
