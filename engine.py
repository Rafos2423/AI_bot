from config import dp, logger


def is_msg(msg):
    return msg != 'Повтор 🔄' and msg != 'Новый чат ⏩' and not msg.startswith('/')


async def set_state(name):
    await dp.current_state().set_state(name)


async def reset_state():
    await dp.current_state().reset_state()


async def change_state(name):
    await reset_state()
    await set_state(name)


def print_log(tag, desc=''):
    inline = desc.replace("\n", "") if desc != '' else ''
    if desc != '':
        inline = f'- {inline}'
    logger.info(f'{tag} {inline}')
