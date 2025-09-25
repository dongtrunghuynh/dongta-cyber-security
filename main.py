# main.py
def choose_backend():
    while True:
        print("Choose storage backend:")
        print("1. In-Memory Store (temporary)")
        print("2. File-Based Store (persistent)")
        print("3. Encrypted File Store (persistent, encrypted)")
        print("4. Database Store (SQLite, persistent)")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            from storage import memory_store as store
            print("Using In-Memory Store (temporary, lost on exit).")
            return store, "In-Memory Store"
        
        elif choice == "2":
            from storage import file_store as store
            print("Using File-Based Store (persistent).")
            return store, "File-Based Store"
        
        elif choice == "3":
            from storage import encrypted_file_store as store
            print("Using Encrypted File Store (persistent, encrypted).")
            return store, "Encrypted File Store"
        
        elif choice == "4":
            from storage import db_store as store
            print("Using Database Store (SQLite, persistent).")
            return store, "Database Store"
        else:
            print("Invalid choice. Please try again.")

def main():
    store, backend_name = choose_backend()
    
    while True:
        print(f"\nSecrets Manager ({backend_name})")
        print("1. Store API Key")
        print("2. Retrieve API Key")
        print("3. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            service = input("Service Name: ")
            api_key = input("API Key: ")
            success = store.store_api_key(service, api_key)
            if success:
                print(f"API Key for {service} stored successfully.")
            else:
                print("Failed to store API Key. Service name and API key cannot be empty.")
        
        elif choice == "2":
            service = input("Service Name: ")
            api_key = store.retrieve_api_key(service)
            if api_key:
                print(f"API Key for {service}: {api_key}")
            else:
                print(f"No API Key found for {service}.")
        
        elif choice == "3":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
