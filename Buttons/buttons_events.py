from aiogram import types
from Generate.generate import msg_history
from Generate.generate_events import correct_generate, clear_history
from config import dp
from engine import change_state
from Buttons.buttons import keyboard_yes_no


@dp.message_handler(lambda x: x.text == 'Повтор 🔄' and len(msg_history) > 1, state='enable')
async def repeat(message):
    repeat = find_last_user_msg()
    await correct_generate(message.from_user.username, repeat, message.answer)


@dp.message_handler(lambda x: x.text == 'Новый чат ⏩' and len(msg_history) > 1, state='enable')
async def new_chat_menu(message):
    theme = f'на тему {msg_history[0]["content"]} ' if msg_history[0]['role'] == 'system' else ''
    await message.answer(f'Память аи {theme}будет очищена. Начать новый чат?', reply_markup=keyboard_yes_no)


@dp.callback_query_handler(text='yes', state='enable')
async def new_chat(query):
    await clear_history(query.from_user.username)
    await query.message.answer(f'Сообщения удалены. Можно выбрать новую тему /start', reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query_handler(text='no', state='new_chat')
async def back(query):
    await change_state('enable')
    await query.message.answer('Давай продолжим')


def find_last_user_msg():
    for msg in msg_history[::-1]:
        if msg['role'] == 'user':
            return msg['content']
