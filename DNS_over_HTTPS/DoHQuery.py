import requests
import sys
import json
import random


def query(domain, headers, dnstype):
    CFI = "https://cloudflare-dns.com/dns-query?name="+domain+"&type="+dnstype
    CFII = "https://1.1.1.1/dns-query?name="+domain+"&type="+dnstype
    GI = "https://dns.google.com/resolve?name="+domain+"&type="+dnstype
    QI = "https://9.9.9.9/dns-query?name="+domain+"&type="+dnstype
    DoHServer = [CFI, CFII, GI, QI]
    url = random.choice(DoHServer)
    print url
    if url is CFII:
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url, headers=headers, verify=False)
        return json.loads(r.text)
    elif url is CFI:
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url, headers=headers, verify=False)
        return json.loads(r.text)
    elif url is QI:
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url, headers=headers, verify=False)
        return json.loads(r.text)
    else:
        r = requests.get(url, headers=headers)
        return json.loads(r.text)


def main(argv):
    headers = {"Accept": "application/dns-json"}
    domain = argv[1]
    dnstype = sys.argv[2] if len(sys.argv) >= 3 else 'A'
    print query(domain, headers, dnstype)


if __name__ == "__main__":
    main(sys.argv)
