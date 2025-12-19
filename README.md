# Website-Basic-Vulnerabilty-Testing
A beginner-friendly Python-based web vulnerability scanner designed to detect common web security issues using real-world payloads. This project focuses on learning offensive security fundamentals, payload handling, and safe vulnerability detection techniques.


🚀 Features

🔎 Cross-Site Scripting (XSS) Detection
Tests reflected XSS using payloads from PayloadsAllTheThings
Supports hundreds of payloads loaded dynamically from files

🧨 SQL Injection (SQLi) Detection
Error-based SQLi scanning
Automatically loads payloads from organized payload folders

🛡 Security Headers Analysis
Detects missing HTTP security headers like CSP, HSTS, X-Frame-Options

📁 Scalable Payload Management
Payloads are stored in folders (payloads/xss, payloads/sqli)
Supports large payload collections without code changes

📄 JSON Report Generation
Scan results are saved in a structured report.json file

🧠 What This Project Teaches

1. How real vulnerability scanners work internally
2. HTTP request handling using Python
3. Payload management at scale
4. Basic vulnerability detection logic
5. Ethical hacking & responsible testing practices

📂Project Structure:

web-vuln-scanner/
├── scanner.py
├── xss.py
├── sqli.py
├── headers.py
├── payloads/
│   ├── xss/
│   └── sqli/
├── report.json
└── requirements.txt

▶️Usage:
pip install -r requirements.txt
python scanner.py

⚠️ Disclaimer:
This tool is for educational purposes only.
Scan only systems you own or have explicit permission to test.
