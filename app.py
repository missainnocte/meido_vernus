# -*- coding: utf-8 -*-

from initializer import init
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
    init_robot()
