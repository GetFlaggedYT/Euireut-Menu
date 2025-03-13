import os
import requests
import subprocess
import time
import shlex

# Colors for different sections
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def show_ascii_art():
    print(f"""
{MAGENTA}███████╗██╗   ██╗██╗███████╗██████╗ ███████╗██╗   ██╗████████╗
{MAGENTA}██╔════╝██║   ██║██║██╔════╝██╔══██╗██╔════╝██║   ██║╚══██╔══╝
{MAGENTA}█████╗  ██║   ██║██║█████╗  ██████╔╝█████╗  ██║   ██║   ██║
{MAGENTA}██╔══╝  ██║   ██║██║██╔══╝  ██╔══██╗██╔══╝  ██║   ██║   ██║
{MAGENTA}███████╗╚██████╔╝██║███████╗██║  ██║███████╗╚██████╔╝   ██║
{MAGENTA}╚══════╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝    ╚═╝
{WHITE}Made by yours truly iNukedYou
{WHITE}Discord: iNukedYou (contact with issues/help)
{WHITE}v0.1
    """)

def check_package_installed(package):
    try:
        subprocess.run([package, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_package(package):
    print(f"{YELLOW}{package} not found. Installing...{RESET}")
    try:
        subprocess.run(["pip", "install", package], check=True)
        print(f"{GREEN}{package} installed successfully.{RESET}")
    except subprocess.CalledProcessError:
        print(f"{RED}Failed to install {package}. Please install it manually.{RESET}")
        return False
    return True

def run_command(command):
    try:
        subprocess.run(shlex.split(command), check=True)
    except subprocess.CalledProcessError as e:
        print(f"{RED}Command error: {e}{RESET}")

def port_scanner(target):
    print(f"{CYAN}Running Port Scanner on {target}{RESET}")
    if not check_package_installed("nmap"):
        if not install_package("nmap"):
            return
    run_command(f"nmap {target}")

def waf_detector(url):
    print(f"{CYAN}Detecting WAF on {url}{RESET}")
    if not check_package_installed("wafw00f"):
        if not install_package("wafw00f"):
            return
    run_command(f"wafw00f {url}")

def icmp_ping(ip):
    print(f"{CYAN}Pinging {ip} to check if it's alive...{RESET}")
    run_command(f"ping -c 4 {ip}")

def whois_lookup(domain):
    print(f"{CYAN}Running Whois Lookup for {domain}{RESET}")
    run_command(f"whois {domain}")

def google_dork(query):
    print(f"{CYAN}Running Google Dork for: {query}{RESET}")
    try:
        response = requests.get(f"https://www.google.com/search?q={query}")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error with Google dorking: {e}{RESET}")

def osint_tool(domain):
    print(f"{CYAN}Running OSINT on {domain}{RESET}")
    if not check_package_installed("theHarvester"):
        if not install_package("theHarvester"):
            return
    run_command(f"theHarvester -d {domain} -b google")

def sniper_exploit(target):
    print(f"{CYAN}Running Sniper Auto Exploiter on {target}{RESET}")
    run_command(f"sniper -t {target}")

def sql_injection_exploit(url):
    print(f"{CYAN}Running SQL Injection Exploit on {url}{RESET}")
    payload = "' OR 1=1 --"
    test_url = f"{url}?id={payload}"
    try:
        response = requests.get(test_url)
        if "error" in response.text or "Warning" in response.text:
            print(f"{GREEN}SQL Injection vulnerability found: {test_url}{RESET}")
        else:
            print(f"{RED}No SQL Injection vulnerability found: {test_url}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}SQL Injection test error: {e}{RESET}")

def xss_exploit(url):
    print(f"{CYAN}Running XSS Exploit on {url}{RESET}")
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?input={payload}"
    try:
        response = requests.get(test_url)
        if payload in response.text:
            print(f"{GREEN}XSS vulnerability found: {test_url}{RESET}")
        else:
            print(f"{RED}No XSS vulnerability found: {test_url}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}XSS test error: {e}{RESET}")

def subdomain_takeover(domain):
    print(f"{CYAN}Checking for subdomain takeover on {domain}{RESET}")
    run_command(f"subjack -w {domain}")

def cloud_security_scanner(domain):
    print(f"{CYAN}Running Cloud Security scan on {domain}{RESET}")
    run_command(f"aws s3 ls s3://{domain}")

def shodan_search(query):
    api_key = os.getenv('SHODAN_API_KEY')
    if not api_key:
        print(f"{RED}Shodan API key not found. Please set the SHODAN_API_KEY environment variable.{RESET}")
        return
    print(f"{CYAN}Running Shodan search for: {query}{RESET}")
    try:
        response = requests.get(f"https://api.shodan.io/shodan/host/{query}?key={api_key}")
        if response.status_code == 200:
            print(f"{GREEN}Shodan results:\n{response.text}{RESET}")
        else:
            print(f"{RED}Error with Shodan search: {response.status_code}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error with Shodan: {e}{RESET}")

def nikto_scan(url):
    print(f"{CYAN}Running Nikto web scanner on {url}{RESET}")
    if not check_package_installed("nikto"):
        if not install_package("nikto"):
            return
    run_command(f"nikto -h {url}")

def metasploit_resource_file(resource_file):
    print(f"{CYAN}Running Metasploit resource file: {resource_file}{RESET}")
    run_command(f"msfconsole -r {resource_file}")

def dns_zone_transfer(domain):
    print(f"{CYAN}Checking DNS Zone Transfer vulnerability on {domain}{RESET}")
    run_command(f"dig axfr @{domain} {domain}")

def ssl_certificate_analysis(domain):
    print(f"{CYAN}Running SSL Certificate Analysis on {domain}{RESET}")
    run_command(f"openssl s_client -connect {domain}:443")

def subdomain_enumeration(domain):
    print(f"{CYAN}Running Subdomain Enumeration on {domain}{RESET}")
    if not check_package_installed("sublist3r"):
        if not install_package("sublist3r"):
            return
    run_command(f"sublist3r -d {domain}")

def directory_brute_force(url):
    print(f"{CYAN}Running Directory Brute Force on {url}{RESET}")
    if not check_package_installed("dirb"):
        if not install_package("dirb"):
            return
    run_command(f"dirb {url}")

def dns_enumeration(domain):
    print(f"{CYAN}Running DNS Enumeration on {domain}{RESET}")
    if not check_package_installed("dnsenum"):
        if not install_package("dnsenum"):
            return
    run_command(f"dnsenum {domain}")

def email_harvesting(domain):
    print(f"{CYAN}Running Email Harvesting on {domain}{RESET}")
    if not check_package_installed("theHarvester"):
        if not install_package("theHarvester"):
            return
    run_command(f"theHarvester -d {domain} -l 500 -b all")

def subdomain_brute_force(domain):
    print(f"{CYAN}Running Subdomain Brute Force on {domain}{RESET}")
    if not check_package_installed("subbrute"):
        if not install_package("subbrute"):
            return
    run_command(f"subbrute {domain}")

def cms_detection(url):
    print(f"{CYAN}Running CMS Detection on {url}{RESET}")
    if not check_package_installed("whatweb"):
        if not install_package("whatweb"):
            return
    run_command(f"whatweb {url}")

def wordpress_user_enumeration(url):
    print(f"{CYAN}Running WordPress User Enumeration on {url}{RESET}")
    if not check_package_installed("wpscan"):
        if not install_package("wpscan"):
            return
    run_command(f"wpscan --url {url} --enumerate u")

def http_header_analysis(url):
    print(f"{CYAN}Running HTTP Header Analysis on {url}{RESET}")
    try:
        response = requests.get(url)
        print(f"{GREEN}HTTP Headers:\n{response.headers}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error with HTTP Header Analysis: {e}{RESET}")

def crawling_and_scraping(url):
    print(f"{CYAN}Running Crawling and Scraping on {url}{RESET}")
    if not check_package_installed("scrapy"):
        if not install_package("scrapy"):
            return
    run_command(f"scrapy crawl {url}")

def vulnerability_scanning(url):
    print(f"{CYAN}Running Vulnerability Scanning on {url}{RESET}")
    if not check_package_installed("openvas"):
        if not install_package("openvas"):
            return
    run_command(f"omp -u admin -w admin --get-results")

def phishing_simulation(email):
    print(f"{CYAN}Running Phishing Simulation on {email}{RESET}")
    if not check_package_installed("SET"):
        if not install_package("SET"):
            return
    run_command(f"setoolkit")

def main_menu():
    clear_screen()
    show_ascii_art()
    print(f"{GREEN}1. Utility Tools{RESET}")
    print(f"{GREEN}2. Networking Tools{RESET}")
    print(f"{GREEN}3. OSINT Tools{RESET}")
    print(f"{GREEN}4. Exploitation Tools{RESET}")
    print(f"{GREEN}5. Additional Tools{RESET}")
    print(f"{RED}6. Exit{RESET}")
    choice = input(f"{YELLOW}Choose an option: {RESET}")
    if choice == "1":
        utility_menu()
    elif choice == "2":
        networking_menu()
    elif choice == "3":
        osint_menu()
    elif choice == "4":
        exploitation_menu()
    elif choice == "5":
        additional_tools_menu()
    elif choice == "6":
        print(f"{RED}Exiting...{RESET}")
        time.sleep(1)
        exit()
    else:
        print(f"{RED}Invalid choice, please try again.{RESET}")
        time.sleep(2)
        main_menu()

def utility_menu():
    clear_screen()
    print(f"{CYAN}1. Whois Lookup{RESET}")
    print(f"{CYAN}2. Google Dork{RESET}")
    print(f"{CYAN}3. OSINT Tool{RESET}")
    print(f"{CYAN}4. Email Harvesting{RESET}")
    print(f"{CYAN}5. Back to Main Menu{RESET}")
    choice = input(f"{YELLOW}Choose an option: {RESET}")
    if choice == "1":
        domain = input(f"{CYAN}Enter domain for Whois lookup: {RESET}")
        whois_lookup(domain)
    elif choice == "2":
        query = input(f"{CYAN}Enter Google dork query: {RESET}")
        google_dork(query)
    elif choice == "3":
        domain = input(f"{CYAN}Enter domain for OSINT lookup: {RESET}")
        osint_tool(domain)
    elif choice == "4":
        domain = input(f"{CYAN}Enter domain for Email Harvesting: {RESET}")
        email_harvesting(domain)
    elif choice == "5":
        main_menu()
    else:
        print(f"{RED}Invalid choice, please try again.{RESET}")
        time.sleep(2)
        utility_menu()

def networking_menu():
    clear_screen()
    print(f"{CYAN}1. Port Scanner{RESET}")
    print(f"{CYAN}2. WAF Detector{RESET}")
    print(f"{CYAN}3. ICMP Ping{RESET}")
    print(f"{CYAN}4. Subdomain Enumeration{RESET}")
    print(f"{CYAN}5. DNS Zone Transfer{RESET}")
    print(f"{CYAN}6. DNS Enumeration{RESET}")
    print(f"{CYAN}7. Subdomain Brute Force{RESET}")
    print(f"{CYAN}8. Back to Main Menu{RESET}")
    choice = input(f"{YELLOW}Choose an option: {RESET}")
    if choice == "1":
        target = input(f"{CYAN}Enter target IP or domain for Port Scan: {RESET}")
        port_scanner(target)
    elif choice == "2":
        url = input(f"{CYAN}Enter URL to detect WAF: {RESET}")
        waf_detector(url)
    elif choice == "3":
        ip = input(f"{CYAN}Enter IP for ICMP ping: {RESET}")
        icmp_ping(ip)
    elif choice == "4":
        domain = input(f"{CYAN}Enter domain for Subdomain Enumeration: {RESET}")
        subdomain_enumeration(domain)
    elif choice == "5":
        domain = input(f"{CYAN}Enter domain for DNS Zone Transfer: {RESET}")
        dns_zone_transfer(domain)
    elif choice == "6":
        domain = input(f"{CYAN}Enter domain for DNS Enumeration: {RESET}")
        dns_enumeration(domain)
    elif choice == "7":
        domain = input(f"{CYAN}Enter domain for Subdomain Brute Force: {RESET}")
        subdomain_brute_force(domain)
    elif choice == "8":
        main_menu()
    else:
        print(f"{RED}Invalid choice, please try again.{RESET}")
        time.sleep(2)
        networking_menu()

def osint_menu():
    clear_screen()
    print(f"{CYAN}1. OSINT Tool{RESET}")
    print(f"{CYAN}2. Shodan Search{RESET}")
    print(f"{CYAN}3. Email Harvesting{RESET}")
    print(f"{CYAN}4. Back to Main Menu{RESET}")
    choice = input(f"{YELLOW}Choose an option: {RESET}")
    if choice == "1":
        domain = input(f"{CYAN}Enter domain for OSINT lookup: {RESET}")
        osint_tool(domain)
    elif choice == "2":
        query = input(f"{CYAN}Enter Shodan search query: {RESET}")
        shodan_search(query)
    elif choice == "3":
        domain = input(f"{CYAN}Enter domain for Email Harvesting: {RESET}")
        email_harvesting(domain)
    elif choice == "4":
        main_menu()
    else:
        print(f"{RED}Invalid choice, please try again.{RESET}")
        time.sleep(2)
        osint_menu()

def exploitation_menu():
    clear_screen()
    print(f"{CYAN}1. SQL Injection Exploit{RESET}")
    print(f"{CYAN}2. XSS Exploit{RESET}")
    print(f"{CYAN}3. Sniper Exploit{RESET}")
    print(f"{CYAN}4. Metasploit Resource File{RESET}")
    print(f"{CYAN}5. Directory Brute Force{RESET}")
    print(f"{CYAN}6. CMS Detection{RESET}")
    print(f"{CYAN}7. WordPress User Enumeration{RESET}")
    print(f"{CYAN}8. Back to Main Menu{RESET}")
    choice = input(f"{YELLOW}Choose an option: {RESET}")
    if choice == "1":
        url = input(f"{CYAN}Enter URL for SQL Injection Exploit: {RESET}")
        sql_injection_exploit(url)
    elif choice == "2":
        url = input(f"{CYAN}Enter URL for XSS Exploit: {RESET}")
        xss_exploit(url)
    elif choice == "3":
        target = input(f"{CYAN}Enter target for Sniper Exploit: {RESET}")
        sniper_exploit(target)
    elif choice == "4":
        resource_file = input(f"{CYAN}Enter Metasploit Resource File path: {RESET}")
        metasploit_resource_file(resource_file)
    elif choice == "5":
        url = input(f"{CYAN}Enter URL for Directory Brute Force: {RESET}")
        directory_brute_force(url)
    elif choice == "6":
        url = input(f"{CYAN}Enter URL for CMS Detection: {RESET}")
        cms_detection(url)
    elif choice == "7":
        url = input(f"{CYAN}Enter URL for WordPress User Enumeration: {RESET}")
        wordpress_user_enumeration(url)
    elif choice == "8":
        main_menu()
    else:
        print(f"{RED}Invalid choice, please try again.{RESET}")
        time.sleep(2)
        exploitation_menu()

def additional_tools_menu():
    clear_screen()
    print(f"{CYAN}1. Nikto Scan{RESET}")
    print(f"{CYAN}2. Cloud Security Scanner{RESET}")
    print(f"{CYAN}3. SSL Certificate Analysis{RESET}")
    print(f"{CYAN}4. HTTP Header Analysis{RESET}")
    print(f"{CYAN}5. Crawling and Scraping{RESET}")
    print(f"{CYAN}6. Vulnerability Scanning{RESET}")
    print(f"{CYAN}7. Phishing Simulation{RESET}")
    print(f"{CYAN}8. Back to Main Menu{RESET}")
    choice = input(f"{YELLOW}Choose an option: {RESET}")
    if choice == "1":
        url = input(f"{CYAN}Enter URL for Nikto Scan: {RESET}")
        nikto_scan(url)
    elif choice == "2":
        domain = input(f"{CYAN}Enter domain for Cloud Security Scan: {RESET}")
        cloud_security_scanner(domain)
    elif choice == "3":
        domain = input(f"{CYAN}Enter domain for SSL Certificate Analysis: {RESET}")
        ssl_certificate_analysis(domain)
    elif choice == "4":
        url = input(f"{CYAN}Enter URL for HTTP Header Analysis: {RESET}")
        http_header_analysis(url)
    elif choice == "5":
        url = input(f"{CYAN}Enter URL for Crawling and Scraping: {RESET}")
        crawling_and_scraping(url)
    elif choice == "6":
        url = input(f"{CYAN}Enter URL for Vulnerability Scanning: {RESET}")
        vulnerability_scanning(url)
    elif choice == "7":
        email = input(f"{CYAN}Enter email for Phishing Simulation: {RESET}")
        phishing_simulation(email)
    elif choice == "8":
        main_menu()
    else:
        print(f"{RED}Invalid choice, please try again.{RESET}")
        time.sleep(2)
        additional_tools_menu()

if __name__ == "__main__":
    main_menu()
