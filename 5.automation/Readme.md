# Automated Incident Response (SOAR Action)

## Overview
To satisfy the automation requirement, a Python containment script (`auto_response.py`) is configured as a **Splunk Alert Trigger Action** for the **"Brute Force Success - Account Compromised"** alert.

## Automated Response Workflow
1. **Trigger Condition:** Splunk detects 5+ failed logins followed by a successful login and `download_customer_data` from an untrusted IP (`45.148.10.23`).
2. **Script Execution:** Splunk passes `$result.src_ip$` and `$result.user$` to `auto_response.py`.
3. **Containment Actions:**
   - **Network Containment:** Executes `ufw deny from 45.148.10.23 to any` to immediately drop all traffic from the attacker's IP.
   - **Account Containment:** Executes `usermod -L admin` to lock the compromised account and revoke active access.
4. **Audit Logging:** Records all automated containment actions with timestamps in `/var/log/soc_automation.log`.

## Sample Execution Output
```text
[2026-11-19 09:04:15] ALERT TRIGGERED: Brute Force Success & Data Exfiltration detected.
[2026-11-19 09:04:15] SUCCESS: Blocked malicious IP 45.148.10.23 via UFW firewall.
[2026-11-19 09:04:16] SUCCESS: Locked compromised user account 'admin'.
```
