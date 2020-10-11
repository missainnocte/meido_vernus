import json
import logging as log
import time

import requests
from requests.exceptions import HTTPError

from config import *
from utils import mirai_api, mirai_of


def auth():
    r = requests.get(mirai_api('/auth'), json={'authKey': MIRAI_KEY})
    return mirai_of(r).get('session')


def verify(session, qq_num):
    r = requests.post(mirai_api('/verify'), json={
        "sessionKey": session,
        "qq": qq_num
    })
    return mirai_of(r)


def send(session, target, msgChain):
    r = requests.post(mirai_api('/sendGroupMessage'), json={
        "sessionKey": session,
        "target": target,
        "messageChain": msgChain
    })
    return mirai_of(r)


def get_session():
    session = auth()
    verify(session)
    return session


def loop_pull(session, callback: function, timeout=10):
    while True:
        r = requests.get(mirai_api('/countMessage'),
                         params={'sessionKey': session})
        count = mirai_of(r).get('data')
        r = requests.get(mirai_api('/fetchLatestMessage'),
                         params={'sessionKey': session, 'count': count})
        msg_list = mirai_of(r).get('data')
        for msg in msg_list:
            callback(msg)
        time.sleep(timeout)
