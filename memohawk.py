import nmap
import random
import re
import os
import subprocess

def scan_network(target):
    """Scan the target network for open ports and services."""
    print(f"Scanning target: {target}")
    scanner = nmap.PortScanner()
    scanner.scan(target, '1-1024', '-sV')
    for host in scanner.all_hosts():
        print(f"Host: {host} ({scanner[host].hostname()})")
        print(f"State: {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"Port: {port}, State: {scanner[host][proto][port]['state']}")
    print("Scan completed.\n")

def check_password_strength(password):
    """Check the strength of a given password."""
    print("Checking password strength...")
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    
    if strength <= 2:
        print("Password Strength: Weak")
    elif 3 <= strength < 5:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Strong")

def random_mac():
    """Generate and change to a random MAC address."""
    print("Generating random MAC address...")
    mac = "02:00:00:" + ":".join(["%02x" % random.randint(0x00, 0x7f) for _ in range(3)])
    print(f"Generated MAC Address: {mac}")
    interface = input("Enter your network interface (e.g., eth0): ")
    try:
        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", mac], check=True)
        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        print(f"MAC address changed successfully to {mac}")
    except Exception as e:
        print(f"Error changing MAC address: {e}")

def main():
    print("Welcome to MemoHawk - A Kali Linux Utility")
    print("1. Network Scan")
    print("2. Password Strength Checker")
    print("3. Random MAC Address Generator")
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "1":
        target = input("Enter the target IP or network (e.g., 192.168.1.0/24): ")
        scan_network(target)
    elif choice == "2":
        password = input("Enter a password to check its strength: ")
        check_password_strength(password)
    elif choice == "3":
        random_mac()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
