import requests
from bs4 import BeautifulSoup

domain = raw_input("What domain do you want to search for? ")
print "Downloading the results."
data = requests.get('https://findsubdomains.com/subdomains-of/' + domain)

# Download the file first via Curl Command
# soup = BeautifulSoup(open("domain.com"), "html.parser")

print "Parsing the document"
soup = BeautifulSoup(data.text, 'html.parser')
data = []
for tr in soup.find_all('a', { 'class': 'aggregated-link mobile-hidden' }):
    data.append(tr.attrs['href'])
print data
