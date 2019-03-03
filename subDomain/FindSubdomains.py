import requests
import sys
from bs4 import BeautifulSoup


def getResults(domain):
    data = requests.get('https://findsubdomains.com/subdomains-of/' + domain)
    soup = BeautifulSoup(data.text, 'html.parser')
    data = []
    for tr in soup.find_all('a', {'class': 'aggregated-link mobile-hidden'}):
        data.append(tr.attrs['href'].split("/")[2])
    return data


def main(argv):
    for i in range(1,len(sys.argv)):
	    domain = sys.argv[i]
        print getResults(domain)


if __name__ == "__main__":
    main(sys.argv)
