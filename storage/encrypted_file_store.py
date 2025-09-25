from cryptography.fernet import Fernet
from utils import io_utils
from pathlib import Path

FILE_PATH = "secrets.enc"
KEY_PATH = "secret.key"

def load_key():
    """Load the encryption key from a file or generate a new one."""
    path = Path(KEY_PATH)
    if path.exists():
        return path.read_bytes()
    key = Fernet.generate_key()
    path.write_bytes(key)
    return key

fernet = Fernet(load_key())

def store_api_key(service, api_key):
    """Store API key in encrypted JSON file."""
    if not service or not api_key:
        return False 
    store = io_utils.read_json_file(FILE_PATH)
    encrypted_key = fernet.encrypt(api_key.encode()).decode()
    store[service] = encrypted_key
    io_utils.write_json_file(FILE_PATH, store)
    return True

def retrieve_api_key(service):
    """Retrieve API key from encrypted JSON file."""
    store = io_utils.read_json_file(FILE_PATH)
    encrypted_key = store.get(service)
    if encrypted_key:
        return fernet.decrypt(encrypted_key.encode()).decode()
    return None
