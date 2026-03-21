import os
from .hash_table import HashTable
from ..storage.record_store import RecordStore
from ..storage.index_store import IndexStore, Recovery

class StorageEngine:
    def __init__(self, data_dir="save_data"):
        os.makedirs(data_dir, exist_ok=True)
        self.record_store = RecordStore(os.path.join(data_dir, "data.log"))
        self.index_store  = IndexStore(os.path.join(data_dir, "index.bin"))
        self.hash_table   = HashTable()
        if not self.index_store.load(self.hash_table):
            Recovery(self.record_store, self.index_store).rebuild(self.hash_table)

    def save(self, record_type, key, data):
        offset = self.record_store.append(record_type, key, data)
        self.hash_table.put(key, offset)
        self.index_store.save(self.hash_table)

    def get(self, key):
        offset = self.hash_table.get(key)
        if offset is None:
            return None
        record = self.record_store.read_at(offset)
        return record.get("data") if record else None

    def delete(self, key):
        offset = self.hash_table.get(key)
        if offset is not None:
            self.record_store.append("delete", key, None)
            removed = self.hash_table.delete(key)
            if removed:
                self.index_store.save(self.hash_table)
            return removed
        return False

    def stats(self):
        return self.hash_table.stats()
