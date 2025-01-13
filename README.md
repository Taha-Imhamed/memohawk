# MemoHawk 🦅

**MemoHawk** is a versatile Kali Linux tool designed to assist cybersecurity professionals and enthusiasts. It combines essential functionalities for network scanning, password strength analysis, and MAC address spoofing.

## Features
1. **Network Scanning and Enumeration**: 
   - Scan target IPs or networks for open ports and services.
   - Uses `nmap` to provide detailed information.

2. **Password Strength Checker**:
   - Evaluates the strength of passwords against basic security criteria.
   - Identifies weak, medium, or strong passwords.

3. **Random MAC Address Generator**:
   - Generates a new MAC address for anonymity.
   - Automatically applies the new MAC to the specified network interface.

## Requirements
- Python 3.7+
- `nmap` Python library
- Administrative privileges for MAC address changes

Install dependencies:
```bash
pip install python-nmap


Usage
Clone the repository:

bash
نسخ الكود
git clone https://github.com/yourusername/memohawk.git
cd memohawk

un the script:

bash
نسخ الكود
sudo python3 memohawk.py

Example Output
Network Scan:

yaml
نسخ الكود
Scanning target: 192.168.1.0/24
Host: 192.168.1.1
State: up
Protocol: tcp
Port: 80, State: open
...
Password Strength Checker:

less
نسخ الكود
Checking password strength...
Password Strength: Strong
Random MAC Address Generator:

less
نسخ الكود
Generating random MAC address...
Generated MAC Address: 02:00:00:4a:6b:1c
MAC address changed successfully to 02:00:00:4a:6b:1c
