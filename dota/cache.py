class DotaCache(object):
    def __init__(self):
        self.matches = set()
        self.users = set()

    def online(self, uid):
        if uid in self.users:
            return True
        self.users.add(uid)
        return False

    def offline(self, uid):
        if uid in self.users:
            self.user.remove(uid)
            return False
        return True

    def has_match(self, mid):
        return mid in self.matches

    def add_match(self, mid):
        if mid in self.matches:
            return False
        self.matches.add(mid)
        return True

DOTA_CACHE = DotaCache()

