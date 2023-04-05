from Generate.data import msg_history, generate, add_msg
from config import dp
from engine import is_msg, print_msg_log, print_scs_log, print_log, reset_state
from Buttons.buttons import keyboard
import time


@dp.message_handler(lambda x: is_msg(x.text), state='enable')
async def get_answer(message):
    print_msg_log(message.from_user.username, message.text, 'ask')
    add_msg('user', message.text)
    try:
        answer = start_generate(message.from_user.username)
        await message.answer(answer, reply_markup=keyboard)
    except BaseException:
        msg_history.clear()
        await reset_state()
        print_log(message.from_user.username, 'clear')
        await message.answer('Количество ответов аи закончилось. Можно начать новый диалог, выбрав новую тему /start', reply_markup=None)


def start_generate(name):
    start = time.time()
    answer = generate()
    duration = round(time.time() - start, 2)
    print_scs_log(name, answer, 'ans', duration)
    add_msg('assistant', answer)
    return answer
