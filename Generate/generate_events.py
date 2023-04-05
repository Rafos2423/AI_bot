from Generate.data import msg_history, generate
from config import dp
from engine import is_msg, print_msg_log, print_scs_log, print_log, reset_state
from Buttons.buttons import keyboard
import time


@dp.message_handler(lambda x: is_msg(x.text), state='enable')
async def get_answer(message):
    await correct_generate(message.from_user.username, message.text, message.answer)


async def correct_generate(name, text, answer):
    try:
        result = start_generate(name, text)
        await answer(result, reply_markup=keyboard)
    except BaseException:
        await clear_history(name)
        await answer('Количество ответов аи закончилось. Можно начать новый диалог, выбрав новую тему /start', reply_markup=None)


def start_generate(name, text):
    print_msg_log(name, text, 'ask')
    start = time.time()
    answer = generate(text)
    duration = round(time.time() - start, 2)
    print_scs_log(name, answer, 'ans', duration)
    return answer


async def clear_history(name):
    msg_history.clear()
    await reset_state()
    print_log(name, 'clear')
