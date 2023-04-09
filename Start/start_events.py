from aiogram.types import ContentType
from Audio.audio_events import get_answer_voice, voice_to_text
from Start.themes import keyboard_themes, themes
from engine import *
from Generate.generate_events import get_answer


@dp.message_handler(lambda x: x.text == '/info', state=[None, 'enable'])
async def info(message):
    await message.answer('Бот позволяет получать ответы с помощью API OpenAI на текстовые и аудио сообщения.\n'
                         'Ограничения на аудио:\n'
                         'Размер: 25 мб\n'
                         'Формат: mp3, mp4, mpeg, mpga, m4a, wav, webm')


@dp.message_handler(commands='start', state=None)
async def start(message):
    await set_state('choose_theme')
    print_log(message.from_user.username, 'start')
    await message.answer('Выбери подходящую тему или назови свою', reply_markup=keyboard_themes)


@dp.message_handler(lambda x: is_msg(x.text))
async def first_state(message):
    print_log(message.from_user.username, 'theme', 'Без темы')
    await set_state('enable')
    await get_answer(message)


@dp.message_handler(content_types=ContentType.VOICE)
async def first_state_voice(message):
    await no_theme(message.from_user.username)
    await get_answer_voice(message)


@dp.callback_query_handler(text=themes, state='choose_theme')
async def choose_theme(query):
    if query.data == 'Без темы':
        await no_theme(query.from_user.username)
        await query.message.answer('Можно и так, задавай вопрос')
    else:
        await set_theme(query.from_user.username, query.data, query.message.answer)


@dp.message_handler(lambda x: is_msg(x.text), state='choose_theme')
async def input_theme(message):
    await set_theme(message.from_user.username, message.text, message.answer)


@dp.message_handler(content_types=ContentType.VOICE, state='choose_theme')
async def first_state_voice(message):
    text = await voice_to_text(message.from_user.username, message.voice.file_id, message.answer)
    await set_theme(message.from_user.username, text, message.answer)


async def set_theme(name, text, answer):
    print_log(name, 'theme', text)
    await set_state('enable')
    await answer('Отлично, я готов к использованию')


async def no_theme(name):
    print_log(name, 'theme', 'Без темы')
    await set_state('enable')
