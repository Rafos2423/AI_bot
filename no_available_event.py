from aiogram.types import ContentType
from config import dp
from engine import is_msg


@dp.message_handler(state='*')
async def start(message):
    if not is_msg(message.text):
        await message.answer(f'Функция {message.text} сейчас не доступна')
    else:
        await message.answer('Сообщения недоступны при настройке')


@dp.message_handler(content_types=ContentType.VOICE, state='*')
async def start(message):
    await message.answer(f'Голосовой ввод сейчас не доступен')
