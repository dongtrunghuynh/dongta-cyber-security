# storage/memory_store.py

_store = {}

def store_api_key(service, api_key):
    """Store API key in Memory"""
    if not service or not api_key:
        print("Service name and API key cannot be empty.")
        return False
    _store[service] = api_key
    return True

def retrieve_api_key(service):
    """Retrieve API key from Memory"""
    return _store.get(service)
    