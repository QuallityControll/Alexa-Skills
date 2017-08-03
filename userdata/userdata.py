from collections import defaultdict

__all__ = ["Userdata"]

class Userdata:
    def __init__(self):
        self.user_history = set()

        self.usernicknames = {}

        self.user_lists = defaultdict(list)##
