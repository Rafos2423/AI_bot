from pydub import AudioSegment
import aiohttp
from aiogram.types import ContentType
from Generate.generate_events import correct_generate, clear_history
from config import bot, dp, api_key
from engine import print_log


@dp.message_handler(content_types=ContentType.VOICE, state='enable')
async def get_answer_voice(message):
    text = await voice_to_text(message.from_user.username, message.voice.file_id, message.answer)
    if not text is None:
        await correct_generate(message.from_user.username, text, message.answer)


async def voice_to_text(name, file_id, answer):
    print_log(name, 'aud')
    tg_file_name = await save(file_id)
    file_name = convert(tg_file_name)
    try:
        text = await send_request(file_name)
        if len(text) == 0:
            raise ValueError
    except ChildProcessError:
        await clear_history(name, 'Закончились токены')
        await answer('Количество ответов аи закончилось. Придется начать новый диалог, выбрав новую тему /start', reply_markup=None)
    except ValueError:
        print_log(name, 'no text')
        await answer('AI не смог распознать сообщение')
    else:
        return text


async def save(file_id):
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_name = f'Audio/files/{file_id}'
    await bot.download_file(file_path, file_name)
    return file_name


def convert(file):
    output_file = f"{file.split('.')[0]}.mp3"
    sound = AudioSegment.from_file(file)
    sound.export(output_file, format="mp3", bitrate="128k")
    return output_file


async def send_request(filename):
    async with aiohttp.ClientSession() as session:
        api_url = 'https://api.openai.com/v1/audio/transcriptions'
        headers = {"Authorization": f"Bearer {api_key}"}
        data = aiohttp.FormData()
        data.add_field('file', open(filename, 'rb'))
        data.add_field('model', 'whisper-1')
        async with session.post(api_url, headers=headers, data=data) as response:
            if response.status == 402:
                raise ChildProcessError
            result = await response.json()
            return result['text']
