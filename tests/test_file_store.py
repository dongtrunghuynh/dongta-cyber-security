import unittest
import os
from storage import file_store

FILE_PATH = "secrets.json"

class TestFileStore(unittest.TestCase):
    
    def setUp(self):
        """Runs before every test. Deletes the JSON file if it exists
        so tests don't interfere with each other."""
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
    
    def tearDown(self):
        """Runs after every test. Deletes the JSON file to clean up."""
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
    
    def test_store_and_retrieve_api_key(self):
        file_store.store_api_key("github", "ghp_12345")
        
        # Instead of printing, we check the file content directly
        with open(FILE_PATH, 'r') as f:
            import json
            data = json.load(f)
            self.assertEqual(data["github"], "ghp_12345")
        
        # Now retrieve and check output
        file_store.retrieve_api_key("github")
    
    def test_retrieve_existing_api_key(self):
        file_store.store_api_key("aws", "aws_secrect")
        
        # Normally retrieve_api_key prints, but we can test the file content directly
        with open(FILE_PATH, 'r') as f:
            import json
            data = json.load(f)
            self.assertEqual(data.get("aws"), "aws_secrect")
        
        file_store.retrieve_api_key("aws")
    
    def test_retrieve_missing(self): 
        file_store.retrieve_api_key("nonexistent")
    
    def test_store_empty_service(self): 
        result = file_store.store_api_key("", "")
        self.assertFalse(result)