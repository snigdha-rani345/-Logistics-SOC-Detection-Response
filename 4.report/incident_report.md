
## End-to-End Attack Investigation & Timeline (MITRE ATT&CK Mapping)

### Executive Summary
During threat hunting on `cold-chain-logs.csv`, a multi-stage external attack was identified originating from IP address **`45.148.10.23` (Russia)**. The attacker conducted a rapid brute-force attack against the `admin` account, successfully authenticated, and exfiltrated sensitive customer records (`download_customer_data`) within a two-minute window. Meanwhile, legitimate user activity (`priya.sharma` from IP `192.168.1.10` in Hyderabad) was verified as normal baseline traffic.

---

### Reconstructed Attack Timeline & MITRE ATT&CK Mapping

| Stage | Timestamp (`2026-11-19`) | Event / Log Evidence | Source IP & Geo-Location | MITRE ATT&CK Tactic | MITRE ATT&CK Technique |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Credential Brute Force** | `09:02:11` – `09:02:41` | 5 consecutive `login,failed` events targeting the `admin` account within 30 seconds | `45.148.10.23` (Russia) | **Credential Access** (`TA0006`) | **T1110** – Brute Force |
| **2. Account Compromise** | `09:03:05` | Successful authentication (`login,success`) into the `admin` account from a foreign location | `45.148.10.23` (Russia) | **Initial Access** (`TA0001`) & **Privilege Escalation** (`TA0004`) | **T1078** – Valid Accounts |
| **3. Data Exfiltration** | `09:04:12` | Unauthorized execution of `download_customer_data` (`status=success`) using the compromised `admin` session | `45.148.10.23` (Russia) | **Collection** (`TA0009`) & **Exfiltration** (`TA0010`) | **T1530** – Data from Cloud Storage / Data Exfiltration |

---

### Investigation Key Takeaways
* **Baseline vs. Malicious Activity:** Legitimate login by `priya.sharma` (`08:01:12`, Hyderabad) was separated from the malicious `admin` login (`09:03:05`, Russia).
* **Post-Exploitation Check:** Executed a Splunk query for PowerShell activity (`action="*powershell*" OR action="*ps*"`), confirming **0 events**—indicating the attacker focused purely on data theft rather than lateral movement or host persistence.
* **Total Attack Duration:** **2 minutes and 1 second** from the first failed login (`09:02:11`) to sensitive data exfiltration (`09:04:12`).
