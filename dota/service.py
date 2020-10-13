import logging as log

from config import *

from .api import get_matches, get_user, refresh
from .cache import DOTA_CACHE


def online():
    users = get_user(list(map(lambda v: str(v[2]), PLAYERS)))
    new_online = []
    for user in users:
        uid = user.get('steamid')
        log.info('获取到{}信息: {}'.format(uid, user))
        if user.get('gameid') == '570':
            if not DOTA_CACHE.online(uid):
                new_online.append(uid)
        else:
            DOTA_CACHE.offline(uid)
    log.info('新在线玩家{}'.format(new_online))
    return new_online


def fetch_matches():
    u_matches = {}
    for (nickname, uid, _) in PLAYERS:
        matches = fetch(uid)
        for m in matches:
            mid = m.get('match_id')
            u = u_matches.get(mid)
            if u:
                u.append(m)
            if not DOTA_CACHE.add_match(mid):
                continue
            if not u:
                u_matches[mid] = [m]
    # print(u_matches)
    return u_matches


def fetch(uid):
    refresh(uid)
    return get_matches(uid)
