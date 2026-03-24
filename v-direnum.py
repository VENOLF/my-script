import requests
from concurrent.futures import ThreadPoolExecutor

print(" __      __")
print(" \\ \\    / /")
print("  \\ \\  / / ")
print("   \\ \\/ /  ")
print("    \\__/   ")
print("   VENOLF")

target = input("\n[+] Enter target (e.g. 192.168.1.1 or example.com): ").strip()
protocol = input("[+] Use HTTPS? (y/n): ").lower()

if protocol == "y":
    base_url = f"https://{target}"
else:
    base_url = f"http://{target}"

# Load wordlist
try:
    with open("wordlist.txt", "r") as f:
        directories = f.read().splitlines()
except FileNotFoundError:
    print("[!] wordlist.txt not found.")
    exit()

# Extensions to try
extensions = ["", ".html", ".php", ".txt"]

def scan(dir_name):
    for ext in extensions:
        url = f"{base_url}/{dir_name}{ext}"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code < 400:
                print(f"[+] Found: {url} ({r.status_code})")
        except requests.exceptions.RequestException:
            pass

# Threading for speed
print("\n[+] Starting scan...\n")

with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(scan, directories)

print("\n[+] Scan complete.")
