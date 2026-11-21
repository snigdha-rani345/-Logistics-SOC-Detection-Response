
# Incident Report: Hidden Attack on ColdChain SOC

## 1. What Happened?
Attacker ne ColdChain server par hidden attack kiya. Pehle brute force se password guess kiya, fir andar ghus ke data chori karne ki koshish ki.

## 2. Timeline - Minute to Minute

| Time | What Happened | MITRE ATT&CK |
| :--- | :--- | :--- |
| 10:00 AM | Attacker ne 50 baar wrong password try kiya | T1110 - Brute Force |
| 10:05 AM | Admin account `coldchain_admin` login ho gaya | T1078 - Valid Accounts |
| 10:07 AM | Attacker ne `whoami` aur `ipconfig` command chalaya | T1087 - Discovery |
| 10:10 AM | Attacker ne `customer_data.csv` download kiya | T1041 - Exfiltration |
| 10:12 AM | Attacker ne apna IP hide karne ke liye logs delete kiye | T1070 - Clear Logs |

## 3. How We Detected?
- Splunk Rule 1: Brute Force Rule ne alert diya
- Splunk Rule 2: Data Exfiltration Rule ne alert diya

## 4. What We Did?
- IP `45.155.204.11` ko BLOCK kiya
- Admin account ko DISABLE kiya
- Password RESET kiya

## 5. False Positive Check
- Total Alerts: 50
- Real Attack: 5
- False Positive: 8 (16% - Less than 20%, So SUCCESS)

## 6. Lessons Learned
- MFA ON karna chahiye tha
- Admin account ko lock karna chahiye
