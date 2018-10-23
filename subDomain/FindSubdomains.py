import requests, sys
from bs4 import BeautifulSoup

domain = sys.argv[1] 
print "Downloading the results."
data = requests.get('https://findsubdomains.com/subdomains-of/' + domain)

# Download the file first via Curl Command
# soup = BeautifulSoup(open("domain.com"), "html.parser")

print "Parsing the document"
soup = BeautifulSoup(data.text, 'html.parser')
data = []
for tr in soup.find_all('a', { 'class': 'aggregated-link mobile-hidden' }):
    data.append(tr.attrs['href'])
print str(data)
