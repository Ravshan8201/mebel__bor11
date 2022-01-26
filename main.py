from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from funct import *
from cons import *
upd = Updater(token=TOKEN, workers=4)
dis = upd.dispatcher
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CommandHandler(command='wwwwww', callback=wwwwww))
dis.add_handler(CommandHandler(command='get_date', callback=get_date))
dis.add_handler(CallbackQueryHandler(pattern='ru_change', callback=ru_change))
dis.add_handler(CallbackQueryHandler(pattern='uz_change', callback=uz_change))
dis.add_handler(CallbackQueryHandler(pattern='ru', callback=ru))
dis.add_handler(CallbackQueryHandler(pattern='uz', callback=uz))
dis.add_handler(MessageHandler(Filters.text, next_func))
dis.add_handler(MessageHandler(Filters.contact, get_contac))
# dis.add_handler(MessageHandler(Filters.location, get_location))
dis.add_handler(MessageHandler(Filters.photo, adm))

def kill(name, sig=signal.SIGTERM):
    """Send a signal to job ``name`` via :func:`os.kill`.

    .. versionadded:: 1.29

    Args:
        name (str): Name of the job
        sig (int, optional): Signal to send (default: SIGTERM)

    Returns:
        bool: `False` if job isn't running, `True` if signal was sent.
    """
    pid = _job_pid(name)
    if pid is None:
        return False

    os.kill(pid, sig)
    return True 

upd.start_polling(drop_pending_updates=True)
