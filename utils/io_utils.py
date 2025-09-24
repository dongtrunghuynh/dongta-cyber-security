import json 
from pathlib import Path

def read_json_file(file_path): 
    """read JSON from file. return {} if files doesnt't exist  or empty."""
    path = Path(file_path)
    if not path.exists() or path.stat().st_size == 0:
        return {}
    try:
        with open(file_path, 'r', encoding="utf-8") as f: 
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        #File exist but is empty or invalid
        return {}
    
    
    
def write_json_file(file_path, data):
    """Write dictionary data to JSON file."""
    path = Path(file_path)
    try:
        with open(path, 'w', encoding="utf-8") as f: 
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")
        return False