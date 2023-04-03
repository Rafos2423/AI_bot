from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import openai
import logging
import sys

openai.api_key = open('Tokens/API_key', 'r').read()
tg_token = open('Tokens/TG_token', 'r').read()

bot = Bot(tg_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('\033[1;0m%(asctime)s - \033[1;32m%(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger('my_logger')
logger.addHandler(handler)
logger.setLevel(logging.INFO)


async def shutdown(dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

shutdown = shutdown(dp)
