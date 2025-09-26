import unittest
import os
from storage import encrypted_file_store
from pathlib import Path
from unittest.mock import patch

FILE_PATH = "secrets.enc"
SALT_PATH = "salt.bin"

class TestEncryptedFileStore(unittest.TestCase):
    def setUp(self):
        # Remove encrypted file and salt before each test
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
        if os.path.exists(SALT_PATH):
            os.remove(SALT_PATH)

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
        if os.path.exists(SALT_PATH):
            os.remove(SALT_PATH)

    @patch('getpass.getpass', return_value='testpass')
    def test_store_and_retrieve_api_key(self, mock_getpass):
        # Store an API key
        result = encrypted_file_store.store_api_key('github', 'ghp_12345')
        self.assertTrue(result)
        self.assertTrue(os.path.exists(FILE_PATH))
        self.assertTrue(os.path.exists(SALT_PATH))

        # Retrieve the API key
        api_key = encrypted_file_store.retrieve_api_key('github')
        self.assertEqual(api_key, 'ghp_12345')

    @patch('getpass.getpass', return_value='testpass')
    def test_store_empty_service_or_key(self, mock_getpass):
        self.assertFalse(encrypted_file_store.store_api_key('', ''))
        self.assertFalse(encrypted_file_store.store_api_key('service', ''))
        self.assertFalse(encrypted_file_store.store_api_key('', 'key'))

    @patch('getpass.getpass', return_value='testpass')
    def test_retrieve_nonexistent_service(self, mock_getpass):
        encrypted_file_store.store_api_key('github', 'ghp_12345')
        api_key = encrypted_file_store.retrieve_api_key('aws')
        self.assertIsNone(api_key)

    @patch('getpass.getpass', side_effect=['testpass', 'wrongpass'])
    def test_wrong_passphrase(self, mock_getpass):
        # Store with correct passphrase
        encrypted_file_store.store_api_key('github', 'ghp_12345')
        # Try to retrieve with wrong passphrase
        api_key = encrypted_file_store.retrieve_api_key('github')
        self.assertIsNone(api_key)

if __name__ == '__main__':
    unittest.main()
