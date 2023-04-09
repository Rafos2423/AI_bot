import aiohttp
import os
from aiogram.types import ContentType
from Generate.generate_events import correct_generate
from config import bot, dp, api_key
from engine import print_log


@dp.message_handler(content_types=[
    ContentType.VOICE,
    ContentType.AUDIO,
    ContentType.DOCUMENT
])
async def voice_message_handler(message):
    file_id = await check(message)
    if file_id is None:
        return

    file_path = await save(message.from_user.username, file_id)
    text = await send_request(file_path)
    os.remove(file_path)
    await correct_generate(message.from_user.username, text, message.answer)


async def check(message):
    if message.content_type == ContentType.VOICE:
        return message.voice.file_id
    elif message.content_type == ContentType.AUDIO:
        return message.audio.file_id
    elif message.content_type == ContentType.DOCUMENT:
        return message.document.file_id
    else:
        await message.answer('Принимаю только текст или аудио')
        return None


async def save(name, file_id):
    print_log(name, 'aud')
    file = await bot.get_file(file_id)
    path = f'Audio/{file.file_path}'
    await bot.download_file(file.file_path, path)
    return path


async def send_request(filename):
    async with aiohttp.ClientSession() as session:
        api_url = 'https://api.openai.com/v1/audio/transcriptions'
        headers = {"Authorization": f"Bearer {api_key}"}
        data = aiohttp.FormData()
        data.add_field('file', open(filename, 'rb'))
        data.add_field('model', 'whisper-1')
        async with session.post(api_url, headers=headers, data=data) as response:
            if response.status == 402:
                raise Exception()
            result = await response.json()
            return result['text']
