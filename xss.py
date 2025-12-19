import requests
from urllib.parse import quote
import os


def load_payloads(path="Payload/XSS"):
    payloads = []
    if not os.path.isdir(path):
        print(f"[!] XSS payload folder not found: {path}")
        return payloads

    for root, _, files in os.walk(path):
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


def scan_xss(url):
    vulnerable = []
    payloads = load_payloads()

    for payload in payloads:
        try:
            encoded = quote(payload)
            test_url = f"{url}?q={encoded}"
            r = requests.get(test_url, timeout=5)

            if payload in r.text or encoded in r.text:
                vulnerable.append({
                    "url": test_url,
                    "payload": payload
                })
        except Exception:
            continue

    return vulnerable
