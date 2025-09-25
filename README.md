# Secrets Manager - Cybersecurity Capstone Project

A Python-based Secrets Manager that allows users to securely store and retrieve API keys or passwords. The project supports **four storage backends**, including encrypted file storage and a SQLite database.

---

## **Features**

1. **In-Memory Store** - Temporary storage in memory (lost on exit).  
2. **File-Based Store** - Persistent storage in plain JSON file.  
3. **Encrypted File Store** - Persistent and encrypted storage using `cryptography`.  
4. **Database Store (SQLite)** - Persistent storage in SQLite database.

---

## **Folder Structure**

secrets_manager/
│
├── main.py
├── secrets.json # optional, created automatically
├── secret.key # optional, created automatically for encrypted store
├── secrets.db # SQLite DB, created automatically
│
├── storage/
│ ├── init.py
│ ├── memory_store.py
│ ├── file_store.py
│ ├── encrypted_file_store.py
│ └── db_store.py
│
└── utils/
├── init.py
└── io_utils.py


---

## **Setup Instructions**

1. Clone or download the repository.  
2. Make sure Python 3.8+ is installed.  
3. Install dependencies (only needed for encrypted store):

```bash
pip install cryptography
```