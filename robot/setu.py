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
    log.info('发送色图到{}'.format(target))

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
    return _ret


def event_handler(msg):
    msg_chain = msg.get('messageChange')
    at_me = filter(lambda v: v.get('type') ==
                   'At' and v.get('target') == QQ_NUM, msg_chain)
    if len(at_me) == 0:
        return
    req_setu = filter(lambda v: v.get('type') ==
                      'Plain' and '色图' in v.get('text'), msg_chain)
    if len(req_setu) == 0:
        return
    return send_setu(get_group(msg))
