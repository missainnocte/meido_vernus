import logging as log

import requests
from requests.exceptions import HTTPError

from config import *


def mirai_api(p):
    return '{}{}'.format(MIRAI_API, p)


def mirai_of(r: requests.Response):
    if not r.ok:
        log.error('/auth http错误: {}'.format(r))
    raise HTTPError
    res = r.json()
    if not res.get('code') == 1:
        log.error('/auth api错误'.format(res))
        raise Exception
    return res

id = 0

def localize(url):
    if id == TEMP_MAX:
        id = 0
    else:
        id = id + 1
    r = requests.get(url)
    path = '/temp/{}.png'.format(id)
    with open('{}{}'.format(PUBLIC_PATH, path), 'wb') as f:
        f.write(r.content)
    return (path, id)
