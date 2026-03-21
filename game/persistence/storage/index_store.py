import os
import json

class IndexStore:
    def __init__(self, filepath):
        self.filepath = filepath

    def save(self, hash_table):
        pairs = list(hash_table.items())
        with open(self.filepath, "w", encoding="utf-8") as f:
            f.write(json.dumps(pairs))

    def load(self, hash_table):
        if not os.path.exists(self.filepath):
            return False
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                pairs = json.loads(f.read())
            for key, offset in pairs:
                hash_table.put(key, offset)
            return True
        except:
            return False

    def exists(self):
        return os.path.exists(self.filepath) and os.path.getsize(self.filepath) > 0


class Recovery:
    def __init__(self, record_store, index_store):
        self.record_store = record_store
        self.index_store = index_store

    def rebuild(self, hash_table):
        temp_list = []
        for offset, record in self.record_store.iter_all():
            key = record.get("key")
            record_type = record.get("type")
            if key:
                is_delete = (record_type == "delete")
                found = False
                for i, (k, o, d) in enumerate(temp_list):
                    if k == key:
                        temp_list[i] = (key, offset, is_delete)
                        found = True
                        break
                if not found:
                    temp_list.append((key, offset, is_delete))
        count = 0
        for key, offset, is_deleted in temp_list:
            if not is_deleted:
                hash_table.put(key, offset)
                count += 1
        self.index_store.save(hash_table)
        return count
