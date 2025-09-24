# storage/file_store.py
from utils import io_utils
import os
from pathlib import Path

FILE_PATH = "secrects.json" # file will becreated in project root

def store_api_key(service, api_key):
    """Store API key in JSON file."""
    if not service or not api_key:
        print("Service name and API key cannot be empty.")
        return False
    store = io_utils.read_json_file(FILE_PATH)
    store[service] = api_key
    io_utils.write_json_file(FILE_PATH, store)
    print(f"API key for {service} stored successfully.")   
    return True

def retrieve_api_key(service):
    """Retrieve API key from JSON file."""
    store = io_utils.read_json_file(FILE_PATH)
    if service in store:
        print(f"API key for '{service}': {store[service]}")
    else:
        print(f"No API key found for '{service}'.")