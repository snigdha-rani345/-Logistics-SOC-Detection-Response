#!/usr/bin/env python3
"""
Splunk Alert Triggered Automated Containment Script
Action: Blocks malicious source IP via UFW firewall and disables compromised user account.
"""

import subprocess
import datetime
import sys

LOG_FILE = "/var/log/soc_automation.log"

def log_action(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    print(entry.strip())
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def block_ip(malicious_ip):
    try:
        # Blocks incoming traffic from the attacker IP on Ubuntu UFW firewall
        subprocess.run(["sudo", "ufw", "deny", "from", malicious_ip, "to", "any"], check=True)
        log_action(f"SUCCESS: Blocked malicious IP {malicious_ip} via UFW firewall.")
    except Exception as e:
        log_action(f"ERROR: Failed to block IP {malicious_ip} - {e}")

def disable_user(username):
    try:
        # Locks the compromised account to stop further unauthorized actions
        subprocess.run(["sudo", "usermod", "-L", username], check=True)
        log_action(f"SUCCESS: Locked compromised user account '{username}'.")
    except Exception as e:
        log_action(f"ERROR: Failed to lock account '{username}' - {e}")

if __name__ == "__main__":
    # Example values passed from Splunk alert payload ($result.src_ip$ and $result.user$)
    attacker_ip = sys.argv[1] if len(sys.argv) > 1 else "45.148.10.23"
    compromised_user = sys.argv[2] if len(sys.argv) > 2 else "admin"

    log_action("ALERT TRIGGERED: Brute Force Success & Data Exfiltration detected.")
    block_ip(attacker_ip)
    disable_user(compromised_user)
