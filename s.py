import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            absolute_url = urljoin(url, href)
            parsed_url = urlparse(absolute_url)
            
            # Filter out non-HTTP(S) links
            if parsed_url.scheme.startswith('http'):
                links.add(absolute_url)
    
    return links

url = input("Enter the URL: ")
links = extract_links(url)

print("Links found:")
for link in links:
    print(link)