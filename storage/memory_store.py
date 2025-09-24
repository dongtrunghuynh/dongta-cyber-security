# storage/memory_store.py
_store = {}

def store_api_key(service, api_key):
    """Store API key in Memory"""
    if not service or not api_key:
        print("Sevice name and API key cannot be empty.")
        return False
    _store[service] = api_key
    print(f"API key for {service} stored successfully.")
    return True

def retrieve_api_key(service):
    """Retrieve API key from Memory"""
    if service in _store:
        print(f"API key for '{service}': {_store[service]}")
    else:
        print(f"No API key found for '{service}'.")
    