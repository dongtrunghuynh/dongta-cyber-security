
def choose_backend():
    while True:
        print("Choose storage backend:")
        print("1. In-Memory Store")
        print("2. File-Based Store")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            from storage import memory_store
            print("Using In-Memory Store (temporary, lost on exit).")
            return memory_store
        
        elif choice == "2":
            from storage import file_store
            print("Using File-Based Store (persistent).")
            return store
        else:
            print("Invalid choice. Please try again.")

def main():
    store = choose_backend()
    while True:
        print("\nSecrects Manager (In Memory)")
        print("1. Store API Key")
        print("2. Retrieve API Key")
        print("3. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            service = input("Service Name: ")
            api_key = input("API Key: ")
            success = memory_store.store_api_key(service, api_key)
            if success:
                print(f"API Key for {service} stored successfully.")
            else:
                print("Failed to store API Key. Service name and API key cannot be empty.")
        
        elif choice == "2":
            service = input("Service Name: ")
            api_key = memory_store.retrieve_api_key(service)
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
        