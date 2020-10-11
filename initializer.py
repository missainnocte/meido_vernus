import logging as log
from datetime import date


def set_logger():
    log.basicConfig(filename=str(date.today()) + '.log',
                    format='%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s', level=log.INFO)

def get_db():
    pass


def init():
    set_logger()
    get_db()
