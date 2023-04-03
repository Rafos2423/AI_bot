from Generate.data import msg_history, generate
from config import dp
from engine import is_msg, print_log
from Buttons.buttons import keyboard
import time


@dp.message_handler(lambda x: is_msg(x.text), state='enable')
async def get_answer(message):
    answer = start_generate(message.text)
    await message.answer(answer, reply_markup=keyboard)


def start_generate(ask):
    msg_history.append({'role': 'user', 'content': ask})
    print_log('txt', ask)
    start = time.time()
    answer = generate()
    duration = round(time.time() - start, 2)
    print_log(f'scs - {duration}s', answer)
    msg_history.append({'role': 'assistant', 'content': answer})
    return answer
