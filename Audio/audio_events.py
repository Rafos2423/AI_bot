from aiogram.types import ContentType
from config import bot, dp


@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"Audio/files/{file_id}.mp3")
