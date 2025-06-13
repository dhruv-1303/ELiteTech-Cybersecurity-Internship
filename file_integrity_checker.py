import hashlib

def calculate_file_hash(filename):
    with open(filename, 'rb') as f:
        file_data = f.read()
        return hashlib.sha256(file_data).hexdigest()

# Set your target file path here
file_path = "/Users/macbookair/Desktop/Internship project/original_hash.txt"

# STEP 1: Generate and save original hash
original_hash = calculate_file_hash(file_path)
with open("original_hash.txt", "w") as hash_file:
    hash_file.write(original_hash)

print("Original hash saved.")

# STEP 2: Re-check hash
new_hash = calculate_file_hash(file_path)

# STEP 3: Compare
if original_hash == new_hash:
    print("✅ File is intact. No changes detected.")
else:
    print("⚠️ File has been modified!")
