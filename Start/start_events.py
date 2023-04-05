from Start.themes import keyboard_themes, themes
from engine import *
from Generate.generate_events import get_answer


@dp.message_handler(lambda x: x.text == '/start' or is_msg(x.text), reply_markup=None)
async def first_state(message):
    if message.text == '/start':
        await set_state('choose_theme')
        await start(message)
    else:
        print_log(message.from_user.username, 'no theme')
        await set_state('enable')
        await get_answer(message)


@dp.message_handler(commands='start', state='choose_theme')
async def start(message):
    print_log(message.from_user.username, 'start')
    await message.answer('Выбери подходящую тему или назови свою', reply_markup=keyboard_themes)


@dp.callback_query_handler(text=themes, state='choose_theme')
async def choose_theme(query):
    if query.data == 'Без темы':
        await query.message.answer('Можно и так, задавай вопрос')
        await reset_state()
    else:
        await set_theme(query.from_user.username, query.message, query.data)


@dp.message_handler(lambda x: is_msg(x.text), state='choose_theme')
async def input_theme(message):
    await set_theme(message.from_user.username, message, message.text)


async def set_theme(name, msg, text):
    add_msg('system', text)
    print_msg_log(name, 'theme', text)
    await change_state('enable')
    await msg.answer('Отлично, я готов к использованию')

