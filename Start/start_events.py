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
        create_theme(query.data)
        print_msg_log(query.from_user.username, query.data, 'theme')
        await change_state('enable')
        await query.message.answer('Отлично, я готов к использованию')


@dp.message_handler(lambda x: is_msg(x.text), state='choose_theme')
async def input_theme(message):
    create_theme(message.text)
    print_msg_log(message.from_user.username, message.text, 'theme')
    await change_state('enable')
    await message.answer('Отлично, я готов к использованию')

