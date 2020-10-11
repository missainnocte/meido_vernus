from concurrent.futures import ThreadPoolExecutor

# from .mirai import loop_pull


def get_callback(callback, threads: ThreadPoolExecutor):
    threads.submit(callback)

def get_sync_hanlde(handlers, threads, session):
    def sync_hanlde(msg):
        for handler in handlers:
            cb = handler(msg)
            if cb:
                threads.submit(cb, session)
    return sync_hanlde
# def create_listener(callbacks, threads: ThreadPoolExecutor):
#     loop_pull()
#     pass
