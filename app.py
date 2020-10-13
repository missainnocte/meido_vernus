# -*- coding: utf-8 -*-

import time

import schedule

from dota.task import status_job
from initializer import get_thread_pool, init
from robot import init as init_robot


def welcome():
    print("""
███╗░░░███╗███████╗██╗██████╗░░█████╗░
████╗░████║██╔════╝██║██╔══██╗██╔══██╗
██╔████╔██║█████╗░░██║██║░░██║██║░░██║
██║╚██╔╝██║██╔══╝░░██║██║░░██║██║░░██║
██║░╚═╝░██║███████╗██║██████╔╝╚█████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝╚═════╝░░╚════╝░ system is launching...
""")


if __name__ == '__main__':
    welcome()
    init()
    thread_pool = get_thread_pool()
    mirai = init_robot(thread_pool)
    dota_status = status_job(thread_pool)
    schedule.every(3).seconds.do(mirai)
    schedule.every().minute.do(dota_status)
    while True:
        schedule.run_pending()
        time.sleep(1)
