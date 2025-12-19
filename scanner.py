from xss import scan_xss
from sqli import scan_sqli
from header import scan_headers
import json


def main():
    print("SCANNER STARTED")
    url = input("Enter target URL: ").strip()
    results = {
        "target": url,
        "xss": scan_xss(url),
        "sqli": scan_sqli(url),
        "headers": scan_headers(url)
    }
    with open("report.json", "w") as f:
        json.dump(results, f, indent=4)
        print("\nScan completed. Report saved to report.json")
        if __name__ == "__main__":
            main()
