import logging as log
import os

import requests
from requests.exceptions import HTTPError

from config import *


def mirai_api(p):
    return '{}{}'.format(MIRAI_API, p)


def mirai_of(r: requests.Response):
    if not r.ok:
        log.error('{} http错误 {}, 请求为 {}'.format(r.url, r.text, r.request.body))
        raise HTTPError
    res = r.json()
    if not res.get('code') == 0:
        log.error('{} api错误 {}, 请求为 {}'.format(r.url, r.text, r.request.body))
        raise Exception
    return res


def localize(url):
    # if id == TEMP_MAX:
    #     id = 0
    # else:
    #     id = id + 1
    log.debug('开始缓存文件, url: {}'.format(url))
    r = requests.get(url)
    filename = url.split('/')[-1]
    path = '/temp/'
    log.debug('缓存文件下载完成, url: {}'.format(url))
    try:
        p = os.path.join(PUBLIC_PATH, path)
        if not os.path.exists(p):
            os.makedirs(p)
        p = os.path.join(p, filename)
        if os.path.isdir(p):
            raise Exception('{}是文件夹'.format(p))
        with open(p, 'wb') as f:
            f.write(r.content)
    except Exception as e:
        log.error(e)
    log.debug('完成缓存文件, url: {}, local: {}'.format(url, path))
    return (path, id)


if __name__ == "__main__":
    for r in range(0, 10):
        print(localize(
            'https://i.pixiv.cat/img-original/img/2018/08/31/20/00/00/70474544_p0.png'))
