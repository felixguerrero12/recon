import requests
import sys
import json


def query(domain, headers, dnstype):
    url = "https://cloudflare-dns.com/dns-query?name="+domain+"&type="+dnstype
    r = requests.get(url, headers=headers, verify=True)
    return json.loads(r.text)


def main(argv):
    headers = {"User-Agent": "Pikachu", "Accept": "application/dns-json"}
    domain = argv[1]
    dnstype = sys.argv[2] if len(sys.argv) >= 3 else 'A'
    print query(domain, headers, dnstype)


if __name__ == "__main__":
    main(sys.argv)
