import os
import platform

def ping(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    cmd = f"ping {param} 1 {ip}"
    response = os.system(cmd)
    if response == 0:
        print(f"✅ Host {ip} is up")
    else:
        print(f"❌ Host {ip} is down")

subnet = input("Enter subnet (e.g., 192.168.1): ")
for i in range(1, 10):  # small range for quick scan
    ping(f"{subnet}.{i}")
