import time

from config import *
from robot.mirai import send

from .api import get_matches, get_user, refresh


def fetch(uid):
    refresh(uid)
    return get_matches(uid)


def match_loop(timeout = 180):
    while True:
        matches = []
        for nickname, uid in PLAYERS:
            matches.append(fetch(uid))
        time.sleep(timeout)

def status_loop(timeout = 30):
    while True:
        user = get_user(list(map(lambda v: v[3], PLAYERS)))
        time.sleep(timeout)

def init(threads):
    threads.submit(match_loop)
    threads.submit(status_loop)
