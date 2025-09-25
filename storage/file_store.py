# storage/file_store.py

import json
from pathlib import Path
from utils import io_utils

FILE_PATH = "secrets.json"  # file will be created in project root

def _read_json_file(file_path):
    """Read JSON from file. Return {} if file doesn't exist or is empty/invalid."""
    path = Path(file_path)
    if not path.exists() or path.stat().st_size == 0:
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # File exists but is invalid JSON
        return {}

def _write_json_file(file_path, data):
    """Write dictionary data to JSON file."""
    path = Path(file_path)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")
        return False

def store_api_key(service, api_key):
    """Store API key in JSON file."""
    if not service or not api_key:
        print("Service name and API key cannot be empty.")
        return False
    store = _read_json_file(FILE_PATH)
    store[service] = api_key
    return _write_json_file(FILE_PATH, store)

def retrieve_api_key(service):
    """Retrieve API key from JSON file."""
    store = _read_json_file(FILE_PATH)
    return store.get(service, None)
