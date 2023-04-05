from aiogram import types
from Generate.data import msg_history, add_msg
from Generate.generate_events import start_generate
from config import dp
from engine import print_log, change_state, reset_state, print_msg_log
from Buttons.buttons import keyboard_yes_no


@dp.message_handler(lambda x: x.text == 'Повтор 🔄' and len(msg_history) > 1, state='enable')
async def repeat(message):
    msg_history.pop()
    msg = msg_history.pop()['content']
    print_msg_log(message.from_user.username, msg, 'rep')
    add_msg('user', message.text)
    answer = start_generate(message.from_user.username)
    await message.answer(answer)


@dp.message_handler(lambda x: x.text == 'Новый чат ⏩' and len(msg_history) > 1, state='enable')
async def new_chat(message):
    theme = f'на тему {msg_history[0]["content"]} ' if msg_history[0]['role'] == 'system' else ''
    await message.answer(f'Память аи {theme}будет очищена. Начать новый чат?', reply_markup=keyboard_yes_no)


@dp.callback_query_handler(text='yes', state='enable')
async def new_chat(query):
    msg_history.clear()
    await reset_state()
    print_log(query.from_user.username, 'clear')
    await query.message.answer(f'Сообщения удалены. Можно выбрать новую тему /start', reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query_handler(text='no', state='new_chat')
async def back(query):
    await change_state('enable')
    await query.message.answer('Давай продолжим')
