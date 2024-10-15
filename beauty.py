from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def links(url, ans):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    arr = []
    for link in soup.find_all('a', href=True):
        full_url = urljoin(url, link["href"]) 
        if len(arr) <= 5 and full_url not in ans:  
            arr.append(full_url)
    return arr

def find(root, depth, ans):
    if depth > 0:
        for url in root:
            arr = links(url, ans)
            ans.extend(arr)
            find(arr, depth - 1, ans)
    return ans

def main(root, depth):
    ans = []
    start_url = root + "index.html"
    ans.append(start_url)

    found_links = find([start_url], depth, ans)

    return found_links

