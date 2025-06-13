# File Integrity Checker - Task 1
# Made as part of ELiteTech Internship (Cyber Security)
# I’m still learning Python and Cyber Security, so made this simple tool to detect if a file has been modified

import hashlib

def get_file_hash(file_path):
    try:
        with open(file_path, "rb") as file:
            content = file.read()
            hash_obj = hashlib.sha256(content)
            return hash_obj.hexdigest()
    except:
        print("Error reading file.")
        return None

def save_original_hash(file_path):
    hash_value = get_file_hash(file_path)
    if hash_value:
        with open("original_hash.txt", "w") as f:
            f.write(hash_value)
        print("Original hash saved!")

def check_file_integrity(file_path):
    current_hash = get_file_hash(file_path)
    try:
        with open("original_hash.txt", "r") as f:
            original_hash = f.read()
        if current_hash == original_hash:
            print("✅ File not changed.")
        else:
            print("⚠️ File was modified!")
    except:
        print("Original hash file not found. Please save hash first.")

# basic menu
print("File Integrity Checker Tool (Internship Task)")
print("1. Save Original File Hash")
print("2. Check File Integrity")
choice = input("Enter choice: ")
path = input("Enter file path: ")

if choice == "1":
    save_original_hash(path)
elif choice == "2":
    check_file_integrity(path)
else:
    print("Invalid choice.")
