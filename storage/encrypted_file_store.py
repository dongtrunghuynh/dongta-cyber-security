# storage/encrypted_file_store.py
import json
import os
from pathlib import Path
import getpass

from cryptography.fernet import Fernet, InvalidToken
from utils import crypto_utils
from utils.crypto_utils import derive_key_from_passphrase

FILE_PATH = "secrets.enc"   # encrypted blob
SALT_PATH = "salt.bin"      # salt used for KDF (binary)

def _ensure_salt():
    """Return salt (create it if missing)."""
    p = Path(SALT_PATH)
    if not p.exists():
        salt = os.urandom(16)
        p.write_bytes(salt)
        return salt
    return p.read_bytes()

def _get_fernet_from_passphrase(passphrase: str):
    salt = _ensure_salt()
    key = derive_key_from_passphrase(passphrase, salt)
    return Fernet(key)

def _read_store(fernet):
    """Return the decrypted dict, or {} if file missing/empty."""
    p = Path(FILE_PATH)
    if not p.exists() or p.stat().st_size == 0:
        return {}
    try:
        ciphertext = p.read_bytes()
        plaintext = fernet.decrypt(ciphertext)
        return json.loads(plaintext.decode())
    except (InvalidToken, ValueError, json.JSONDecodeError):
        # InvalidToken => wrong passphrase or corrupted file
        raise

def _write_store(fernet, store_dict):
    plaintext = json.dumps(store_dict).encode()
    ciphertext = fernet.encrypt(plaintext)
    Path(FILE_PATH).write_bytes(ciphertext)

def store_api_key(service, api_key):
    """Store API key encrypted in secrets.enc. Returns True on success."""
    if not service or not api_key:
        return False

    passphrase = getpass.getpass("Enter master passphrase (used to encrypt): ")
    fernet = _get_fernet_from_passphrase(passphrase)

    # load existing store (if any)
    try:
        store = _read_store(fernet)
    except InvalidToken:
        # Wrong passphrase for existing file
        print("Error: wrong passphrase for existing encrypted store.")
        return False

    store[service] = api_key
    _write_store(fernet, store)
    return True

def retrieve_api_key(service):
    """Retrieve and decrypt API key for service. Returns string or None."""
    if not Path(FILE_PATH).exists():
        return None

    passphrase = getpass.getpass("Enter master passphrase: ")
    fernet = _get_fernet_from_passphrase(passphrase)

    try:
        store = _read_store(fernet)
    except InvalidToken:
        print("Error: wrong passphrase or corrupted encrypted file.")
        return None

    return store.get(service)

