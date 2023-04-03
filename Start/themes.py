from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

themes = ['Создание', 'Общение', 'Перевод', 'Править', 'Анализ',
          'Поиск', 'План', 'Код', 'Без темы']


keyboard_themes = InlineKeyboardMarkup().add(
        InlineKeyboardButton('Создание', callback_data='Создание'),
        InlineKeyboardButton('Общение', callback_data='Общение'),
        InlineKeyboardButton('Перевод', callback_data='Перевод'),
        InlineKeyboardButton('Править', callback_data='Править'),
        InlineKeyboardButton('Анализ', callback_data='Анализ'),
        InlineKeyboardButton('Поиск', callback_data='Поиск'),
        InlineKeyboardButton('План', callback_data='План'),
        InlineKeyboardButton('Код', callback_data='Код'),
        InlineKeyboardButton('Без темы', callback_data='Без темы'))



