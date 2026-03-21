import os
from .encode_decode import encode, decode

class RecordStore:
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            open(self.filepath, "wb").close()

    def append(self, record_type, key, data):
        encoded = encode(record_type, key, data)
        with open(self.filepath, "ab") as f:
            offset = f.tell()
            f.write(encoded)
        return offset

    def read_at(self, offset):
        try:
            with open(self.filepath, "rb") as f:
                f.seek(offset)
                return decode(f.readline())
        except:
            return None

    def iter_all(self):
        try:
            with open(self.filepath, "rb") as f:
                while True:
                    offset = f.tell()
                    line = f.readline()
                    if not line:
                        break
                    record = decode(line)
                    if record:
                        yield (offset, record)
        except:
            return
