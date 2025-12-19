import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security"
]


def scan_headers(url):
    missing = []

    try:
        r = requests.get(url, timeout=5)
        for header in SECURITY_HEADERS:
            if header not in r.headers:
                missing.append(header)
    except Exception:
        pass

    return missing
