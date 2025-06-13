import socket

def scan_ports(target, ports):
    print(f"🔍 Scanning {target} for open ports...")
    for port in ports:
        sock = socket.socket()
        sock.settimeout(1)
        try:
            sock.connect((target, port))
            print(f"✅ Port {port} is open")
        except:
            pass
        finally:
            sock.close()

if __name__ == "__main__":
    target = input("Enter target IP (e.g. 127.0.0.1): ")
    ports = [21, 22, 23, 80, 443, 8080]
    scan_ports(target, ports)
