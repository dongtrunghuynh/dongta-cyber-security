# utils/io_utils.py
import json
from pathlib import Path

def read_json_file(file_path):
    path = Path(file_path)
    if not path.exists() or path.stat().st_size == 0:
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def write_json_file(file_path, data):
    path = Path(file_path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return True
