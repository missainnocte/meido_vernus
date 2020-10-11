import json
import logging as log
import time

import requests
from config import *
from requests.exceptions import HTTPError
from utils import mirai_api, mirai_of


def auth():
    r = requests.post(mirai_api('/auth'), json={'authKey': MIRAI_KEY})
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
    verify(session, QQ_NUM)
    return session


def get_loop_pull(session):
    def _loop(callback, timeout=3):
        while True:
            r = requests.get(mirai_api('/countMessage'),
                            params={'sessionKey': session})
            count = mirai_of(r).get('data')
            if not count == 0:
                r = requests.get(mirai_api('/fetchLatestMessage'),
                                params={'sessionKey': session, 'count': count})
                log.info('获取到{}条消息: {}'.format(count, r.text))
                msg_list = mirai_of(r).get('data')
                for msg in msg_list:
                    callback(msg)
            time.sleep(timeout)
    return _loop

def get_group(msg):
    return msg['sender']['group']['id']
