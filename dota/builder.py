import random

from config import *

from .contents import ONLINE_MSG


def online_msg(uids):
    arr = []
    # if len(uids) == 0:
    #     return
    for p in PLAYERS:
        if str(p[2]) in uids:
            arr.append(p[0])
    msg = random.choice(ONLINE_MSG).format(','.join(arr))
    return msg
