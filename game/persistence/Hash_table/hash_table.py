from .hash_entry import HashEntry

class HashTable:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity
        self.collisions = 0

    def _hash(self, key):
        h = 5381
        for c in key:
            h = ((h << 5) + h) + ord(c)
            h = h & 0xFFFFFFFF
        return h % self.capacity

    def load_factor(self):
        return self.size / self.capacity

    def put(self, key, offset):
        index = self._hash(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                node.offset = offset
                return
            node = node.next
        if self.buckets[index] is not None:
            self.collisions += 1
        entry = HashEntry(key, offset)
        entry.next = self.buckets[index]
        self.buckets[index] = entry
        self.size += 1
        if self.load_factor() > 0.7:
            self._rehash()

    def get(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.offset
            node = node.next
        return None

    def delete(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[index] = node.next
                self.size -= 1
                return True
            prev = node
            node = node.next
        return False

    def _rehash(self):
        old_buckets = self.buckets
        old_capacity = self.capacity
        self.capacity = self.capacity * 2
        self.buckets = [None] * self.capacity
        self.size = 0
        self.collisions = 0
        for i in range(old_capacity):
            node = old_buckets[i]
            while node:
                self.put(node.key, node.offset)
                node = node.next

    def items(self):
        for i in range(self.capacity):
            node = self.buckets[i]
            while node:
                yield (node.key, node.offset)
                node = node.next

    def stats(self):
        occupied = sum(1 for b in self.buckets if b is not None)
        return (
            ("capacity", self.capacity),
            ("size", self.size),
            ("load_factor", round(self.load_factor(), 4)),
            ("collisions", self.collisions),
            ("occupied_buckets", occupied),
        )
