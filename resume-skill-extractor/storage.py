import json
from datetime import datetime
import os

STORAGE_FILE = "stored_resumes.jsonl"

def save_result(data, path=STORAGE_FILE):
    data["timestamp"] = str(datetime.now())
    with open(path, "a") as f:
        f.write(json.dumps(data) + "\n")

def load_all_resumes(path=STORAGE_FILE):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return [json.loads(line) for line in f.readlines()]
