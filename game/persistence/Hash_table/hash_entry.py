class HashEntry:
    def __init__(self, key, offset):
        self.key = key
        self.offset = offset
        self.next = None
