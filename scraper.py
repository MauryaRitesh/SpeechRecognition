import requests
from bs4 import BeautifulSoup

search_item = 'what is python'  ## search query
url = "https://www.google.co.in/search?q=" + search_item

response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")

for item in soup.select(".r a"):
    print (item.text)
    break
