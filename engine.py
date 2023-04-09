from config import dp, logger
from colorama import Fore


def is_msg(msg):
    return msg != 'Повтор 🔄' and msg != 'Новый чат ⏩' and not msg.startswith('/')


async def set_state(name=''):
    await dp.current_state().reset_state()
    if name != '':
        await dp.current_state().set_state(name)


def print_log(name, tag='', text='', duration=''):
    dash = Fore.WHITE + '-'
    tag = f'{dash} {color_tag(tag)}'

    if text != '':
        text = text.replace('\n', '')
        text = f'{dash} {Fore.LIGHTMAGENTA_EX + str(len(text))} ' \
               f'{dash} {Fore.LIGHTWHITE_EX + text}'
    if duration != '':
        duration = f'{dash} {Fore.LIGHTCYAN_EX + str(duration)}s '

    logger.info(f'@{name} {tag} {duration}{text}')


def color_tag(tag):
    if tag == 'clear':
        return Fore.LIGHTRED_EX + f'{tag}'
    elif tag == 'ans':
        return Fore.LIGHTGREEN_EX + f'{tag}'
    else:
        return Fore.LIGHTYELLOW_EX + f'{tag}'
