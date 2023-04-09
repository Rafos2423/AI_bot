import shutil
import pyperclip
from Generate.generate import msg_history, generate
from engine import *
from Buttons.buttons import keyboard
import time


@dp.message_handler(lambda x: is_msg(x.text), state='enable')
async def get_answer(message):
    await correct_generate(message.from_user.username, message.text, message.answer)


async def correct_generate(name, text, answer):
    try:
        pyperclip.copy(text)
        result = await start_generate(name, text)
        pyperclip.copy(result)
    except ChildProcessError:
        await clear_history(name, 'Закончились токены')
        await answer('Количество ответов аи закончилось. Придется начать новый диалог, выбрав новую тему /start', reply_markup=None)
    else:
        await answer(result, reply_markup=keyboard)


async def start_generate(name, text):
    print_log(name, 'ask', text)
    start = time.time()
    answer = await generate(text)
    duration = round(time.time() - start, 2)
    print_log(name, 'ans', answer, duration)
    return answer


async def clear_history(name, reason):
    msg_history.clear()
    await set_state()
    print_log(name, 'clear', reason)
    try:
        shutil.rmtree('Audio/files')
    except FileNotFoundError:
        pass
