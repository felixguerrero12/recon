import json, requests, sys

def getResults(domain):
    r = requests.get('https://crt.sh/?q=%.' + domain + '&output=json')
    data = []
    for item in r.json():
	data.append(item['name_value'])
    return data

def main(argv):
    for i in range(1,len(sys.argv)):
	output = ""
	print "*******************************************************************"
	print "*              Certificate Search for " + sys.argv[i] + "*"
	print "*******************************************************************"
	domain = sys.argv[i]
	output = sorted(set(getResults(domain)))
	print '\n'.join(output)


if __name__ == "__main__":
    main(sys.argv)
