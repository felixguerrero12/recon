# recon

1. Use findsubdomains.py to search for subdomains using https://findsubdomains.com/.
2. Use getSubdomains_SSL.py to extract subjectAltName from SSL Certificates.
  Example: python3 getcert.py www.riotgames.com | jq -r '.notAfter, .subjectAltName[][1]'
