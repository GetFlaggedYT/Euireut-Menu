# ⚠️ Ethical Warning ⚠️

This tool is intended for educational and ethical penetration testing purposes only.
	•	Do not use this tool without explicit permission from the target owner.
	•	Unauthorized use against websites, networks, or services that you do not own or have permission to test is illegal and punishable by law.
	•iNukedYou (Developer) is not responsible for any misuse or illegal activity performed using this tool.

⸻

# 📜 Features & Menu Options

Once executed, the tool presents a main menu with multiple categories:

### 1️⃣ Utility Tools
	•	Whois Lookup - Retrieves domain registration information
	•	Google Dork - Finds indexed sensitive information
	•	OSINT Tool - Extracts open-source intelligence
	•	Email Harvesting - Collects emails from public sources

### 2️⃣ Networking Tools
	•	Port Scanner (Nmap) - Scans open ports on a target
	•	WAF Detector (wafw00f) - Identifies Web Application Firewalls
	•	ICMP Ping - Checks if a target is online
	•	Subdomain Enumeration - Finds subdomains of a target domain
	•	DNS Enumeration - Identifies DNS records
	•	DNS Zone Transfer Test - Checks for misconfigured DNS servers

### 3️⃣ OSINT Tools
	•	OSINT Reconnaissance (theHarvester)
	•	Shodan Search - Queries Shodan for exposed hosts
	•	Metadata Extraction - Analyzes metadata of public files

### 4️⃣ Exploitation Tools
	•	SQL Injection Tester - Attempts SQL injection attacks
	•	XSS Injection Tester - Tests for XSS vulnerabilities
	•	CMS Detection - Identifies a website’s CMS
	•	WordPress User Enumeration - Lists WordPress users
	•	Metasploit Resource Runner - Automates Metasploit attacks

### 5️⃣ Additional Security Tools
	•	Nikto Scan - Performs web vulnerability scanning
	•	Cloud Security Scanner - Checks exposed cloud storage buckets
	•	SSL Certificate Analysis - Validates SSL configurations
	•	HTTP Header Analysis - Extracts security headers

⸻

# 🖥️ Supported Platforms

EUIERUT is compatible with:
	•	Linux (Debian, Ubuntu, Kali, Arch, etc.)
	•	macOS
	•	Windows (via WSL or native Python environment)
	•	iSH (iOS terminal emulator – limited functionality due to sandboxing)

⸻

# 🛠️ Installation

### 1. Clone the repository<br/>
 
   `git clone https://github.com/inukedyou1/Euireut-Menu.git </br>
cd Euireut-Menu`

### 2.Install dependencies

Ensure you have Python 3.x installed. Then, install the required modules:
`pip install -r requirements.txt`

### 3.  Additional Dependencies

Some tools require external dependencies:

•	Install nmap, wafw00f, theHarvester, nikto, dirb, and others based on your OS:
 
• Debian-based (Ubuntu/Kali):<br/>
`sudo apt install nmap wafw00f theharvester nikto dirb dnsenum`

•	Arch Linux:<br/>
`sudo pacman -S nmap wafw00f theharvester nikto`

•	Windows (WSL):<br/>
`sudo apt install nmap wafw00f theharvester nikto`

•	iSH (iOS terminal):<br/>
`apk add nmap wafw00f theharvester nikto`

# 🚀 Usage

Run the tool with:<br/>
`python3 euierut.py`
