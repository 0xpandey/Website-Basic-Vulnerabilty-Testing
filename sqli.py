import requests
import os

SQL_ERRORS = [
    "sql syntax",
    "mysql",
    "syntax error",
    "unterminated"
]


def load_payloads_from_folder(folder_path="Payload/SQLI"):
    payloads = []

    if not os.path.isdir(folder_path):
        print(f"[!] SQLi payload folder not found: {folder_path}")
        return payloads

    for root, _, files in os.walk(folder_path):
        for name in files:
            if name.lower().endswith((".txt", ".md")):
                try:
                    file_path = os.path.join(root, name)
                    with open(
                        file_path,
                        "r",
                        encoding="utf-8",
                        errors="ignore"
                    ) as f:

                        for line in f:
                            line = line.strip()
                            if line and not line.startswith("#"):
                                payloads.append(line)
                except Exception:
                    continue

    return list(dict.fromkeys(payloads))


def scan_sqli(url):
    vulnerable = []
    payloads = load_payloads_from_folder()

    for payload in payloads:
        try:
            test_url = f"{url}?id={payload}"
            r = requests.get(test_url, timeout=5)

            for err in SQL_ERRORS:
                if err.lower() in r.text.lower():
                    vulnerable.append({
                        "url": test_url,
                        "payload": payload
                    })
                    break
        except Exception:
            continue

    return vulnerable
