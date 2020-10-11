# -*- coding: utf-8 -*-
import atexit
from concurrent.futures import ThreadPoolExecutor

from config import *

from .event import get_sync_hanlde
from .mirai import get_loop_pull, get_session, send
from .setu import event_handler as setu_handler


def send_bye():
    # send([{
    #     'type': 'Plain',
    #     'text': '暂时离开~'
    # }])
    pass


def init(pool):
    s = get_session()
    atexit.register(send_bye)
    loop_pull = get_loop_pull(s)
    arr = [setu_handler]
    # thread_pool = ThreadPoolExecutor(THREAD_POOL)
    event_handler = get_sync_hanlde(arr, pool, s)
    loop_pull(event_handler)
