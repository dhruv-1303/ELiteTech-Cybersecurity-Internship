import socket

target = input("Enter target IP: ")
port = int(input("Enter port (e.g., 21, 80): "))

try:
    s = socket.socket()
    s.connect((target, port))
    s.settimeout(2)
    banner = s.recv(1024)
    print(f"📥 Banner: {banner.decode().strip()}")
except:
    print("❌ Could not grab banner")
