import requests
import sys
import json
import random

def query(domain, headers, dnstype):
    cfurl = "https://cloudflare-dns.com/dns-query?name="+domain+"&type="+dnstype
    gurl = "https://dns.google.com/resolve?name="+domain+"&type="+dnstype
    DoHServer = [cfurl, gurl]
    url = random.choice(DoHServer)
    r = requests.get(url, headers=headers, verify=True)
    return json.loads(r.text)


def main(argv):
    headers = {"User-Agent": "Pikachu", "Accept": "application/dns-json"}
    domain = argv[1]
    dnstype = sys.argv[2] if len(sys.argv) >= 3 else 'A'
    print query(domain, headers, dnstype)


if __name__ == "__main__":
    main(sys.argv)