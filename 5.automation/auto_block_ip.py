# SOAR Automation - Auto Block Malicious IP
# This script blocks IP when Brute Force detected

import json

def block_ip(ip_address):
    print(f"Blocking IP: {ip_address}")
    # In real Splunk SOAR, this will call Firewall API
    # firewall.block(ip_address)
    print(f"IP {ip_address} BLOCKED Successfully")
    return True

def disable_user(username):
    print(f"Disabling User: {username}")
    # In real SOAR, this will disable AD account
    # ad.disable_user(username)
    print(f"User {username} DISABLED Successfully")
    return True

# Example - Hidden Attack Data
malicious_ip = "45.155.204.11"
compromised_user = "coldchain_admin"

# Step 1: If Brute Force > 5 attempts, Block IP
print("Alert Received: Brute Force Detected")
block_ip(malicious_ip)

# Step 2: Disable Compromised Account
disable_user(compromised_user)

print("SOAR Playbook Executed - Attack Stopped")
