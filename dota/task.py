import time
from concurrent.futures import ThreadPoolExecutor

from config import *
from robot.mirai import send

from .api import get_matches, get_user, refresh
from .builder import online_msg
from .service import online


def fetch(uid):
    refresh(uid)
    return get_matches(uid)


def match_job(pool: ThreadPoolExecutor):
    # while True:
    def _job():
        matches = []
        for nickname, uid in PLAYERS:
            matches .append(fetch(uid))
    pool.submit(_job)
    # time.sleep(timeout)


def status_job(pool):
    # while True:
    def wrapper():
        def _job():
            users = online()
            msg = online_msg(users)
            send(msg)
        pool.submit(_job)
    return wrapper
    # time.sleep(timeout)

# def init(threads):
    # threads.submit(match_loop)
    # threads.submit(status_loop)
