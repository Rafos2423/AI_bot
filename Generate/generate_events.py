from config import dp
from engine import print_log, is_msg
from Generate.data import start_generate
from Buttons.buttons import keyboard


@dp.message_handler(lambda x: is_msg(x.text), state='enable')
async def get_answer(message):
    answer = start_generate(message.text)
    await message.answer(answer, reply_markup=keyboard)
