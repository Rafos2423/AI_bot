from Generate.data import msg_history, generate
from config import dp
from engine import is_msg, print_msg_log, print_scs_log, print_log, reset_state
from Buttons.buttons import keyboard
import time


@dp.message_handler(lambda x: is_msg(x.text), state='enable')
async def get_answer(message):
    print_msg_log(message.from_user.username, message.text, 'ask')
    msg_history.append({'role': 'user', 'content': message.text})
    try:
        print(len(msg_history))
        answer = start_generate(message.from_user.username)
        await message.answer(answer, reply_markup=keyboard)
    except BaseException:
        await clear_history(message.from_user.username)
        await message.answer('Количество ответов аи закончилось. Можно начать новый диалог, выбрав новую тему /start', reply_markup=None)


def start_generate(name):
    start = time.time()
    answer = generate()
    duration = round(time.time() - start, 2)
    print_scs_log(name, answer, 'ans', duration)
    msg_history.append({'role': 'assistant', 'content': answer})
    return answer


async def clear_history(name):
    msg_history.clear()
    await reset_state()
    print_log(name, 'clear')
