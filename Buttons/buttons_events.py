from aiogram import types
from Generate.generate import msg_history
from Generate.generate_events import correct_generate, clear_history
from config import dp
from Buttons.buttons import keyboard_yes_no
from engine import set_state, take_user_id


@dp.message_handler(lambda x: x.text == 'Повтор 🔄', state='enable')
async def repeat(message):
    user_id = take_user_id(message.from_user)
    if len(msg_history[user_id]) < 2:
        await message.answe('Сначала начните диалог')
        return
    rep = find_last_user_msg(user_id)
    await correct_generate(message.from_user, rep, message.answer)


@dp.message_handler(lambda x: x.text == 'Новый чат ⏩', state='enable')
async def new_chat_menu(message):
    user_id = take_user_id(message.from_user)
    await set_state('choose')
    theme = f'на тему {msg_history[user_id][0]["content"]} ' if msg_history[user_id][0]['role'] == 'system' else ''
    await message.answer(f'Память аи {theme}будет очищена. Начать новый чат?', reply_markup=keyboard_yes_no)


@dp.callback_query_handler(text='yes', state='choose')
async def new_chat(query):
    await clear_history(query.from_user, 'Нажата кнопка')
    await query.message.answer(f'Сообщения удалены. Можно выбрать новую тему /start', reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query_handler(text='no', state='choose')
async def back(query):
    await set_state('enable')
    await query.message.answer('Давай продолжим')


def find_last_user_msg(id):
    for msg in msg_history[id][::-1]:
        if msg['role'] == 'user':
            return msg['content']
