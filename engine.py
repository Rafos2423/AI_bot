from Generate.generate import add_msg
from config import dp, logger
from colorama import Fore


def is_msg(msg):
    return msg != 'Повтор 🔄' and msg != 'Новый чат ⏩' and not msg.startswith('/')


async def set_state(name):
    await dp.current_state().set_state(name)


async def reset_state():
    await dp.current_state().reset_state()


async def change_state(name):
    await reset_state()
    await set_state(name)


def print_log(name, tag):
    if tag == 'clear':
        tag = Fore.LIGHTRED_EX + f'{tag}'
    logger.info(f'@{name} - {Fore.LIGHTYELLOW_EX + tag}')


def print_msg_log(name, text, tag):
    text = text.replace("\n", "")
    logger.info(f'@{name} {dash} {Fore.LIGHTYELLOW_EX + tag} {dash} {Fore.LIGHTMAGENTA_EX + str(len(text))} {dash} {Fore.LIGHTWHITE_EX + text}')


def print_scs_log(name, text, tag, duration):
    text = text.replace("\n", "")
    logger.info(f'@{name} {dash} {Fore.LIGHTGREEN_EX + tag} {dash} {Fore.LIGHTMAGENTA_EX + str(len(text))} {dash} {Fore.LIGHTCYAN_EX + str(duration)}s {dash} {Fore.LIGHTWHITE_EX + text}')


dash = Fore.WHITE + '-'
