from Generate.generate import msg_history, generate
from engine import *
from Buttons.buttons import keyboard
import time


@dp.message_handler(lambda x: is_msg(x.text), state='enable')
async def get_answer(message):
    await correct_generate(message.from_user.username, message.text, message.answer)


async def correct_generate(name, text, answer):
    try:
        result = await start_generate(name, text)
    except:
        await clear_history(name)
        await answer('Количество ответов аи закончилось. Придется начать новый диалог, выбрав новую тему /start', reply_markup=None)
    else:
        await answer(result, reply_markup=keyboard)


async def start_generate(name, text):
    print_msg_log(name, text, 'ask')
    start = time.time()
    answer = await generate(text)
    duration = round(time.time() - start, 2)
    print_scs_log(name, answer, 'ans', duration)
    return answer


async def clear_history(name):
    msg_history.clear()
    await reset_state()
    print_log(name, 'clear')
