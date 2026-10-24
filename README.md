# 🚀 SentinelSIEM Dashboard

A real-time SIEM (Security Information and Event Management) dashboard built using HTML, CSS, and JavaScript to simulate a modern SOC (Security Operations Center).

---

## 🔗 Live Project
👉 https://github.com/dhavalnt19/SIEM/siem_dashboard.html

---

## 📸 Dashboard Preview

### 🧭 Overview
![Overview](overview.png)

### 🚨 Alerts Feed
![Alerts](alerts.png)

### 📜 Log Stream
![Logs](logs.png)

### 🧠 MITRE ATT&CK Matrix
![MITRE](mitre.png)

---

## 💡 Features

- 🔴 Real-time alert monitoring (Critical, High, Medium, Info)
- 📡 Live log streaming simulation
- 🧠 MITRE ATT&CK matrix visualization
- ⚙️ Detection rule engine (toggle-based)
- 🌍 Attack origin tracking (geo insights)
- 📊 Event volume analytics (24h)
- 🖥️ Asset inventory with risk scoring

---

## 🛠️ Tech Stack

- HTML  
- CSS  
- JavaScript  

---

## 🎯 Purpose

This project was built to:
- Understand SIEM workflows  
- Simulate SOC dashboard environments  
- Practice security data visualization  
- Improve frontend + cybersecurity integration  

---

## 📌 Future Improvements

- Backend log ingestion (Node.js / Python)
- Real-time WebSocket integration
- Authentication system
- Database for persistent logs

---





# Azure Sentinel Enterprise SOC Lab

## Overview

This project demonstrates enterprise-scale Microsoft Sentinel detection engineering using realistic datasets generated for Azure cloud environments.

## Features

- 1.5M+ security events
- Azure Activity
- Entra ID Sign-ins
- Windows Security
- Firewall
- DNS
- Web Logs
- Threat Intelligence

## Detection Engineering

- 25 Analytics Rules
- 100+ KQL Queries
- 15 MITRE ATT&CK Techniques
- 10 Sentinel Workbooks

## Technologies

- Microsoft Sentinel
- Azure Monitor
- KQL
- Python
- Azure Log Analytics

## Repository Structure

```text
analytics_rules/
mitre/
kql/
datasets/
workbooks/
```

## Screenshots

(Add Sentinel screenshots here)

## MITRE Coverage

| Technique | Detection |
|-----------|-----------|
| T1078 | Password Spray |
| T1110 | Brute Force |
| T1059.001 | PowerShell |

---x---x---x---


# Password Spray Detection

## Severity

High

## Data Source

Entra ID Sign-in Logs

## MITRE ATT&CK

- T1110 - Brute Force
- T1078 - Valid Accounts

## Description

Detects multiple failed login attempts against many accounts from a single IP.

## KQL

```kusto
SigninLogs
| summarize FailedAttempts=count() by IPAddress
| where FailedAttempts > 20
```

## Investigation

- Review affected accounts.
- Check MFA status.
- Identify source IP.
- Correlate with Threat Intelligence.

## Response

- Block source IP.
- Reset affected accounts.
- Require MFA.



...
...
...
...

## 🙌 Feedback

Feel free to open issues or suggest improvements!
