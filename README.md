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



