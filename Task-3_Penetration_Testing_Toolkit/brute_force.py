def mock_login(username, password):
    correct_username = "admin"
    correct_password = "1234"
    return username == correct_username and password == correct_password

usernames = ["admin", "root"]
passwords = ["123", "1234", "admin"]

for user in usernames:
    for pwd in passwords:
        print(f"Trying {user}:{pwd}")
        if mock_login(user, pwd):
            print(f"✅ Login successful with {user}:{pwd}")
            exit()
print("❌ No valid credentials found.")
