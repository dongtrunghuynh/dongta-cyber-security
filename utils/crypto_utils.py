# utils/crypto_utils.py
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

def derive_key_from_passphrase(passphrase: str, salt: bytes) -> bytes:
    """
    Derive a URL-safe base64-encoded 32-byte key from a passphrase and salt,
    suitable for use with cryptography.fernet.Fernet.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(passphrase.encode()))
