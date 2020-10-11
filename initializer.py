import logging as log
from concurrent.futures import ThreadPoolExecutor
from datetime import date

from config import *


def set_logger():
    log.basicConfig(filename=str(date.today()) + '.log',
                    format='%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s', level=log.DEBUG)


def get_db():
    pass


def get_thread_pool():
    return ThreadPoolExecutor(THREAD_POOL)


def init():
    set_logger()
    get_db()
