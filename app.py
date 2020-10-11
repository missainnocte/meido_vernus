# -*- coding: utf-8 -*-

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
    init_robot(thread_pool)
