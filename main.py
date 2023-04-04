from aiogram.utils import executor
from config import *

try:
    import Start.start_events
    import Buttons.buttons_events
    import Generate.generate_events
    import no_available_event

    executor.start_polling(dp, on_shutdown=shutdown)
except BaseException:
    print('error')
