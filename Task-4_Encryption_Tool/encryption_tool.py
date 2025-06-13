from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted = f.decrypt(encrypted_data)
    original_filename = filename.replace(".enc", "")
    with open("decrypted_" + original_filename, "wb") as file:
        file.write(decrypted)

if __name__ == "__main__":
    print("\n--- Advanced Encryption Tool ---")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        generate_key()
        print("✅ Key generated and saved as secret.key")
    elif choice == "2":
        filename = input("Enter filename to encrypt: ")
        key = load_key()
        encrypt_file(filename, key)
        print("✅ File encrypted successfully!")
    elif choice == "3":
        filename = input("Enter .enc filename to decrypt: ")
        key = load_key()
        decrypt_file(filename, key)
        print("✅ File decrypted successfully!")
    else:
        print("❌ Invalid choice")
