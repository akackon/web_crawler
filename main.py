import requests
from bs4 import BeautifulSoup

def looky_spider():
    count = 1
    url = "https://unsplash.com/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,features="html.parser")
    while count <= 5:
        for link in soup.find_all("img",{"class":"YVj9w"}):
            print(link.get("alt"))
            count += 1


looky_spider()