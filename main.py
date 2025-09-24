from storage import memory_store

def main():
    while True:
        print("\nSecrects Manager (In Memory)")
        print("1. Store API Key")
        print("2. Retrieve API Key")
        print("3. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            service = input("Service Name: ")
            api_key = input("API Key: ")
            memory_store.store_api_key(service, api_key)
            print(f"API Key for {service} stored successfully.")
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
        