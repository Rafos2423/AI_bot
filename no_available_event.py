from config import dp
from engine import is_msg


@dp.message_handler(state='*')
async def start(message):
    if not is_msg(message.text):
        await message.answer(f'Функция {message.text} сейчас не доступна')
    else:
        await message.answer('Сообщения недоступны при настройке')
