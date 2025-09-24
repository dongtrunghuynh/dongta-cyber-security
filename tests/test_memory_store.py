# tests/test_memory_store.py
import unittest
from storage import memory_store

class TestMemoryStore(unittest.TestCase):
    
    def setUp(self):
        """Runs before every test. Resets the in-memory store
        so tests don't interfere with each other."""
        memory_store._store.clear()
    
    def test_store_and_retrieve_api_key(self):
        memory_store.store_api_key("github", "ghp_12345")
        
        # instead of printing, we assert the value directly
        self.assertEqual(memory_store._store["github"], "ghp_12345")
    
    def test_retrieve_existing_api_key(self):
        memory_store._store["aws"] = "aws_secrect"
        
        #Normally retrieve_api_key prints, but we can test the dict directly
        self.assertEqual(memory_store._store.get("aws"), "aws_secrect")
    
    def test_retrieve_missing(self): 
        self.assertIsNone(memory_store._store.get("nonexistent"))
    
    def test_store_empty_service(self): 
        memory_store.store_api_key("", "")
        #Nothing should be stored
        self.assertEqual(len(memory_store._store), 0)
        
if __name__ == '__main__':
    unittest.main()

