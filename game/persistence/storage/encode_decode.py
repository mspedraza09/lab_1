import json

def encode(record_type, key, data):
    record = {"type": record_type, "key": key, "data": data}
    return (json.dumps(record) + "\n").encode("utf-8")

def decode(raw):
    try:
        line = raw.decode("utf-8").strip()
        return json.loads(line) if line else None
    except:
        return None
