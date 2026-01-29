import sys
import socket

print(" __      __")
print(" \\ \\    / /")
print("  \\ \\  / / ")
print("   \\ \\/ /  ")
print("    \\__/   ")
print("   VENOLF")

ip = input("ENTER TARGET IP: ")
ports = range(1, 1025)
open_ports = []

def probe_ports(ip, port, result=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = 0
        sock.close()
    except Exception as e:
        print(f"The error is : {e}")
    return result

for port in ports:
    sys.stdout.flush()
    response = probe_ports(ip, port)
    if response == 0:
        open_ports.append(port)

if open_ports:
    print(f"\nOpen Ports on {ip} are:")
    print(sorted(open_ports))
else:
    print("\nNo open ports found.")
