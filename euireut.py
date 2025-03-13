
import os
import requests
import subprocess
import time
import shlex
import logging


logging.basicConfig(filename='tool.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"

def clear_screen():
    """Clear the terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")

def show_ascii_art():
    """Display ASCII art for the tool."""
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
    """Check if a package is installed."""
    try:
        subprocess.run([package, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_package(package):
    """Install a package using the appropriate command based on the OS."""
    logging.info(f"Attempting to install {package}...")
    print(f"{YELLOW}{package} not found. Installing...{RESET}")
    try:
        if os.name == "posix":  
            subprocess.run(["sudo", "apt-get", "install", package, "-y"], check=True)
        else:  
            subprocess.run(["pip", "install", package], check=True)
        print(f"{GREEN}{package} installed successfully.{RESET}")
        logging.info(f"{package} installed successfully.")
    except subprocess.CalledProcessError:
        print(f"{RED}Failed to install {package}. Please install it manually.{RESET}")
        logging.error(f"Failed to install {package}.")
        return False
    return True

def prompt_install(package):
    """Prompt the user to install a missing package."""
    print(f"{RED}THIS TOOL NEEDS {package} INSTALLED, ARE YOU SURE YOU WANT TO INSTALL?{RESET}")
    print(f"{YELLOW}1. Yes{RESET}")
    print(f"{YELLOW}2. No, return to menu{RESET}")
    choice = input(f"{YELLOW}Choose an option: {RESET}")
    if choice == "1":
        return install_package(package)
    elif choice == "2":
        return False
    else:
        print(f"{RED}Invalid choice, returning to menu.{RESET}")
        return False

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(shlex.split(command), check=True)
    except subprocess.CalledProcessError as e:
        print(f"{RED}Command error: {e}{RESET}")
        logging.error(f"Command error: {e}")

def validate_url(url):
    """Validate the URL format."""
    if not url.startswith(('http://', 'https://')):
        print(f"{RED}Invalid URL format. Please include http:// or https://.{RESET}")
        return False
    return True

def validate_email(email):
    """Basic email validation."""
    if "@" not in email or "." not in email.split("@")[-1]:
        print(f"{RED}Invalid email format.{RESET}")
        return False
    return True

def port_scanner(target):
    """Run a port scan on the specified target."""
    print(f"{CYAN}Running Port Scanner on {target}{RESET}")
    if not check_package_installed("nmap"):
        if not prompt_install("nmap"):
            return
    run_command(f"nmap {target}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def waf_detector(url):
    """Detect WAF on the specified URL."""
    if not validate_url(url):
        return
    print(f"{CYAN}Detecting WAF on {url}{RESET}")
    if not check_package_installed("wafw00f"):
        if not prompt_install("wafw00f"):
            return
    run_command(f"wafw00f {url}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def icmp_ping(ip):
    """Ping the specified IP address."""
    print(f"{CYAN}Pinging {ip} to check if it's alive...{RESET}")
    run_command(f"ping -c 4 {ip}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def whois_lookup(domain):
    """Perform a WHOIS lookup for the specified domain."""
    print(f"{CYAN}Running Whois Lookup for {domain}{RESET}")
    run_command(f"whois {domain}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def google_dork(query):
    """Perform a Google Dork search."""
    print(f"{CYAN}Running Google Dork for: {query}{RESET}")
    try:
        response = requests.get(f"https://www.google.com/search?q={query}")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error with Google dorking: {e}{RESET}")
        logging.error(f"Error with Google dorking: {e}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def osint_tool(domain):
    """Run OSINT on the specified domain."""
    print(f"{CYAN}Running OSINT on {domain}{RESET}")
    if not check_package_installed("theHarvester"):
        if not prompt_install("theHarvester"):
            return
    run_command(f"theHarvester -d {domain} -b google")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def sniper_exploit(target):
    """Run Sniper Auto Exploiter on the specified target."""
    print(f"{CYAN}Running Sniper Auto Exploiter on {target}{RESET}")
    run_command(f"sniper -t {target}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def sql_injection_exploit(url):
    """Run SQL Injection Exploit on the specified URL."""
    if not validate_url(url):
        return
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
        logging.error(f"SQL Injection test error: {e}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def xss_exploit(url):
    """Run XSS Exploit on the specified URL."""
    if not validate_url(url):
        return
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
        logging.error(f"XSS test error: {e}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def reverse_ip_lookup(ip):
    """Perform a Reverse IP Lookup for the specified IP address."""
    print(f"{CYAN}Performing Reverse IP Lookup for {ip}{RESET}")
    try:
        response = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error with Reverse IP Lookup: {e}{RESET}")
        logging.error(f"Error with Reverse IP Lookup: {e}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def http_status_code_checker(url):
    """Check the HTTP Status Code for the specified URL."""
    if not validate_url(url):
        return
    print(f"{CYAN}Checking HTTP Status Code for {url}{RESET}")
    try:
        response = requests.get(url)
        print(f"{GREEN}HTTP Status Code: {response.status_code}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error checking HTTP Status Code: {e}{RESET}")
        logging.error(f"Error checking HTTP Status Code: {e}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def basic_authentication_scanner(url):
    """Check for Basic Authentication on the specified URL."""
    if not validate_url(url):
        return
    print(f"{CYAN}Checking for Basic Authentication on {url}{RESET}")
    try:
        response = requests.get(url)
        if response.status_code == 401:
            print(f"{GREEN}Basic Authentication required for {url}{RESET}")
        else:
            print(f"{RED}No Basic Authentication found for {url}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error checking Basic Authentication: {e}{RESET}")
        logging.error(f"Error checking Basic Authentication: {e}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def data_breach_checker(email):
    """Check for data breaches for the specified email."""
    if not validate_email(email):
        return
    print(f"{CYAN}Checking for data breaches for {email}{RESET}")
    try:
        response = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}")
        if response.status_code == 200:
            breaches = response.json()
            print(f"{GREEN}Data breaches found for {email}:")
            for breach in breaches:
                print(f"- {breach['Name']} ({breach['Domain']})")
        elif response.status_code == 404:
            print(f"{GREEN}No data breaches found for {email}.")
        else:
            print(f"{RED}Error checking data breaches: {response.status_code}{RESET}")
            logging.error(f"Error checking data breaches: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error with data breach check: {e}{RESET}")
        logging.error(f"Error with data breach check: {e}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def subdomain_takeover(domain):
    """Check for subdomain takeover on the specified domain."""
    print(f"{CYAN}Checking for subdomain takeover on {domain}{RESET}")
    run_command(f"subjack -w {domain}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def cloud_security_scanner(domain):
    """Run a Cloud Security scan on the specified domain."""
    print(f"{CYAN}Running Cloud Security scan on {domain}{RESET}")
    run_command(f"aws s3 ls s3://{domain}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def shodan_search(query):
    """Run a Shodan search for the specified query."""
    api_key = os.getenv('SHODAN_API_KEY')
    if not api_key:
        print(f"{RED}Shodan API key not found. Please set the SHODAN_API_KEY environment variable.{RESET}")
        logging.error("Shodan API key not found.")
        return
    print(f"{CYAN}Running Shodan search for: {query}{RESET}")
    try:
        response = requests.get(f"https://api.shodan.io/shodan/host/{query}?key={api_key}")
        if response.status_code == 200:
            print(f"{GREEN}Shodan results:\n{response.text}{RESET}")
        else:
            print(f"{RED}Error with Shodan search: {response.status_code}{RESET}")
            logging.error(f"Error with Shodan search: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error with Shodan: {e}{RESET}")
        logging.error(f"Error with Shodan: {e}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def nikto_scan(url):
    """Run Nikto web scanner on the specified URL."""
    if not validate_url(url):
        return
    print(f"{CYAN}Running Nikto web scanner on {url}{RESET}")
    if not check_package_installed("nikto"):
        if not prompt_install("nikto"):
            return
    run_command(f"nikto -h {url}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def metasploit_resource_file(resource_file):
    """Run a Metasploit resource file."""
    print(f"{CYAN}Running Metasploit resource file: {resource_file}{RESET}")
    run_command(f"msfconsole -r {resource_file}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def dns_zone_transfer(domain):
    """Check DNS Zone Transfer vulnerability on the specified domain."""
    print(f"{CYAN}Checking DNS Zone Transfer vulnerability on {domain}{RESET}")
    run_command(f"dig axfr @{domain} {domain}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def ssl_certificate_analysis(domain):
    """Run SSL Certificate Analysis on the specified domain."""
    print(f"{CYAN}Running SSL Certificate Analysis on {domain}{RESET}")
    run_command(f"openssl s_client -connect {domain}:443")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def subdomain_enumeration(domain):
    """Run Subdomain Enumeration on the specified domain."""
    print(f"{CYAN}Running Subdomain Enumeration on {domain}{RESET}")
    if not check_package_installed("sublist3r"):
        if not prompt_install("sublist3r"):
            return
    run_command(f"sublist3r -d {domain}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def directory_brute_force(url):
    """Run Directory Brute Force on the specified URL."""
    if not validate_url(url):
        return
    print(f"{CYAN}Running Directory Brute Force on {url}{RESET}")
    if not check_package_installed("dirb"):
        if not prompt_install("dirb"):
            return
    run_command(f"dirb {url}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def dns_enumeration(domain):
    """Run DNS Enumeration on the specified domain."""
    print(f"{CYAN}Running DNS Enumeration on {domain}{RESET}")
    if not check_package_installed("dnsenum"):
        if not prompt_install("dnsenum"):
            return
    run_command(f"dnsenum {domain}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def email_harvesting(domain):
    """Run Email Harvesting on the specified domain."""
    print(f"{CYAN}Running Email Harvesting on {domain}{RESET}")
    if not check_package_installed("theHarvester"):
        if not prompt_install("theHarvester"):
            return
    run_command(f"theHarvester -d {domain} -l 500 -b all")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def subdomain_brute_force(domain):
    """Run Subdomain Brute Force on the specified domain."""
    print(f"{CYAN}Running Subdomain Brute Force on {domain}{RESET}")
    if not check_package_installed("subbrute"):
        if not prompt_install("subbrute"):
            return
    run_command(f"subbrute {domain}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def cms_detection(url):
    """Run CMS Detection on the specified URL."""
    if not validate_url(url):
        return
    print(f"{CYAN}Running CMS Detection on {url}{RESET}")
    if not check_package_installed("whatweb"):
        if not prompt_install("whatweb"):
            return
    run_command(f"whatweb {url}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def wordpress_user_enumeration(url):
    """Run WordPress User Enumeration on the specified URL."""
    if not validate_url(url):
        return
    print(f"{CYAN}Running WordPress User Enumeration on {url}{RESET}")
    if not check_package_installed("wpscan"):
        if not prompt_install("wpscan"):
            return
    run_command(f"wpscan --url {url} --enumerate u")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def http_header_analysis(url):
    """Run HTTP Header Analysis on the specified URL."""
    if not validate_url(url):
        return
    print(f"{CYAN}Running HTTP Header Analysis on {url}{RESET}")
    try:
        response = requests.get(url)
        print(f"{GREEN}HTTP Headers:\n{response.headers}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error with HTTP Header Analysis: {e}{RESET}")
        logging.error(f"Error with HTTP Header Analysis: {e}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def crawling_and_scraping(url):
    """Run Crawling and Scraping on the specified URL."""
    if not validate_url(url):
        return
    print(f"{CYAN}Running Crawling and Scraping on {url}{RESET}")
    if not check_package_installed("scrapy"):
        if not prompt_install("scrapy"):
            return
    run_command(f"scrapy crawl {url}")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def vulnerability_scanning(url):
    """Run Vulnerability Scanning on the specified URL."""
    if not validate_url(url):
        return
    print(f"{CYAN}Running Vulnerability Scanning on {url}{RESET}")
    if not check_package_installed("openvas"):
        if not prompt_install("openvas"):
            return
    run_command(f"omp -u admin -w admin --get-results")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def phishing_simulation(email):
    """Run Phishing Simulation on the specified email."""
    if not validate_email(email):
        return
    print(f"{CYAN}Running Phishing Simulation on {email}{RESET}")
    if not check_package_installed("SET"):
        if not prompt_install("SET"):
            return
    run_command(f"setoolkit")
    input(f"{YELLOW}Press any key to return to the main menu...{RESET}")
    main_menu()

def main_menu():
    """Display the main menu and handle user input."""
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
        logging.info("Exiting the tool.")
        time.sleep(1)
        exit()
    else:
        print(f"{RED}Invalid choice, please try again.{RESET}")
        logging.warning("Invalid choice in main menu.")
        time.sleep(2)
        main_menu()

def utility_menu():
    """Display the utility tools menu and handle user input."""
    clear_screen()
    print(f"{CYAN}1. Whois Lookup{RESET}")
    print(f"{CYAN}2. Google Dork{RESET}")
    print(f"{CYAN}3. OSINT Tool{RESET}")
    print(f"{CYAN}4. Email Harvesting{RESET}")
    print(f"{CYAN}5. HTTP Status Code Checker{RESET}")
    print(f"{CYAN}6. Reverse IP Lookup{RESET}")
    print(f"{CYAN}7. Data Breach Checker{RESET}")
    print(f"{CYAN}8. Back to Main Menu{RESET}")
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
        url = input(f"{CYAN}Enter URL for HTTP Status Code Check: {RESET}")
        http_status_code_checker(url)
    elif choice == "6":
        ip = input(f"{CYAN}Enter IP for Reverse IP Lookup: {RESET}")
        reverse_ip_lookup(ip)
    elif choice == "7":
        email = input(f"{CYAN}Enter email for Data Breach Check: {RESET}")
        data_breach_checker(email)
    elif choice == "8":
        main_menu()
    else:
        print(f"{RED}Invalid choice, please try again.{RESET}")
        logging.warning("Invalid choice in utility menu.")
        time.sleep(2)
        utility_menu()

def networking_menu():
    """Display the networking tools menu and handle user input."""
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
        logging.warning("Invalid choice in networking menu.")
        time.sleep(2)
        networking_menu()

def osint_menu():
    """Display the OSINT tools menu and handle user input."""
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
        logging.warning("Invalid choice in OSINT menu.")
        time.sleep(2)
        osint_menu()

def exploitation_menu():
    """Display the exploitation tools menu and handle user input."""
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
        logging.warning("Invalid choice in exploitation menu.")
        time.sleep(2)
        exploitation_menu()

def additional_tools_menu():
    """Display the additional tools menu and handle user input."""
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
        logging.warning("Invalid choice in additional tools menu.")
        time.sleep(2)
        additional_tools_menu()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}Exiting...{RESET}")
        logging.info("Tool exited by user.")
        exit()
    except Exception as e:
        print(f"{RED}An unexpected error occurred: {e}{RESET}")
        logging.error(f"Unexpected error: {e}")
