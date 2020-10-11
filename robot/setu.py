# -*- coding: utf-8 -*-
import logging as log

import requests
from config import *
from utils import localize

from .mirai import get_group, send

session = None


def down_setu(id):
    r = requests.get(SETU_API)
    res = r.json()
    print(res)
    img = requests.get(res['data'][0]['url'])
    path = '{}/{}.png'.format(PUBLIC_PATH, id)
    with open(path, 'wb') as f:
        f.write(img.content)


def send_setu(target):
    log.info('开始发送色图到{}'.format(target))

    def _ret(s):
        r = requests.get(SETU_API).json()
        for img in r.get('data'):
            p = LOCAL_SERVER + localize(img.get('url'))
            send(s, target, [{
                'type': 'Plain',
                'text': '色图time!'
            }, {
                'type': 'Image',
                'url': p
            }])
            log.info('完成发送色图到{}, 色图: {}'.format(target, img.get('url')))
    return _ret


def event_handler(msg):
    msg_chain = msg.get('messageChain')
    if not is_at_me(msg_chain):
        return
    if not is_req_setu(msg_chain):
        return
    return send_setu(get_group(msg))


def is_at_me(msg_ch):
    flt = filter(lambda v: v.get('type') ==
                   'At' and v.get('target') == QQ_NUM, msg_ch)
    if len(list(flt)) == 0:
        return False
    return True


def is_req_setu(msg_ch):
    flt = filter(lambda v: v.get('type') ==
                   'Plain' and '色图' in v.get('text'), msg_ch)
    if len(list(flt)) == 0:
        return False
    return True
