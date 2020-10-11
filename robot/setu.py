# -*- coding: utf-8 -*-

import asyncio
import datetime
import json
import logging as log
import os
import time

import aiohttp
import requests
from aiohttp import ClientSession

from config import *
from mirai import loop_pull, send

session = None


def down_setu(id):
    r = requests.get(SETU_API)
    res = r.json()
    print(res)
    img = requests.get(res['data'][0]['url'])
    path = '{}/{}.png'.format(PUBLIC_PATH, id)
    with open(path, 'wb') as f:
        f.write(img.content)


def del_setu(id):
    path = '{}/{}.png'.format(PUBLIC_PATH, id)
    if os.path.exists(path):
        os.remove(path)


def get_session():
    r_auth = requests.post(MIRAI_API + '/auth',
                           data=json.dumps({'authKey': 'INITKEYiCVswvf9'}))
    if not check_err(r_auth):
        return
    session = r_auth.json()['session']
    log.info('获取session:' + session)
    r_verify = requests.post(MIRAI_API + '/verify', data=json.dumps({
        "sessionKey": session,
        "qq": QQ_NUM
    }))
    if not check_err(r_auth):
        return
    return session


def send_setu(target, id, session):
    down_setu(id)
    r = requests.post(MIRAI_API + '/sendGroupMessage', data=json.dumps({
        "sessionKey": session,
        "target": target,
        "messageChain": [
            {"type": "Plain", "text": "色图Time!"},
            {"type": "Image", "url": "http://127.0.0.1/{}.png".format(id)}
        ]
    }))
    print(r.text)
    del_setu(id)


def check_err(r: requests.Response):
    if not r.ok:
        log.error('请求{}错误: {}'.format(r.url, r.status_code) + r.text)
        return False
    j = r.json()
    if j['code'] != 0:
        log.error('API错误:{}'.format(j))
        return False
    return True


def set_log():
    log.basicConfig(filename=str(datetime.date.today(
    )) + '.log', format='%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s', level=log.INFO)


def loop_event(session):
    id = 0
    while True:
        path = '{}/countMessage?sessionKey={}'.format(MIRAI_API, session)
        r_count = requests.get(path).json().get('data')
        msgs = requests.get(
            '{}/fetchLatestMessage?sessionKey={}&count={}'.format(MIRAI_API, session, r_count)).json().get('data')
        for msg in msgs:
            mcs = msg.get('messageChain')
            if not mcs:
                continue
            for mc in mcs:
                text = mc.get('display')
                if not text:
                    continue
                need_setu = False
                if '@{}'.format(NICKNAME) in text:
                    need_setu = True
                if need_setu:
                    send_setu(msg['sender']['group']['id'], id, session)
                    id = id + 1
        time.sleep(10)


def start():
    session = get_session()
    loop_event(session)


if __name__ == "__main__":
    session = get_session()
    loop_event(session)


def event_handler(msg):
    pass


# def loop(session):
#     loop_pull(session, event_handler, 5)
