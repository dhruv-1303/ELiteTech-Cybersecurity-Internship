# Task 1 – File Integrity Checker

This script verifies if a file has been modified by comparing its original and current hash values.

## 🔐 Objective
To detect unauthorized or accidental changes in files using SHA-256 hashing.

---

## 🧠 How It Works
1. It reads a file (e.g., `test_file.txt`)
2. Calculates its hash using SHA-256
3. Saves the original hash in `original_hash.txt`
4. When run again, it recalculates and compares the current hash with the original

---

## ▶️ How to Run

1. Create a test file named `test_file.txt` in the same folder as the script.
2. Run the script using Python:
```bash
python file_integrity_checker.py
