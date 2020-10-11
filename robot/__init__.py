import atexit
from concurrent.futures import ThreadPoolExecutor

import setu

from ..config import *
from .event import get_sync_hanlde
from .mirai import get_loop_pull, get_session, send


def send_bye():
    # send([{
    #     'type': 'Plain',
    #     'text': '暂时离开~'
    # }])
    pass


def init():
    s = get_session()
    atexit.register(send_bye)
    loop_pull = get_loop_pull(s)
    arr = [setu.event_handler]
    thread_pool = ThreadPoolExecutor(THREAD_POOL)
    event_handler = get_sync_hanlde(arr, thread_pool, s)
    loop_pull(event_handler)
