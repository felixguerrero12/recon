import requests
import sys
from bs4 import BeautifulSoup


def getResults(IPAddr):
    r = requests.get('https://api.hackertarget.com/reverseiplookup/?q=' + IPAddr)
    return r.text


def main(argv):
    IPAddr = sys.argv[1]
    print getResults(IPAddr)


if __name__ == "__main__":
    main(sys.argv)
