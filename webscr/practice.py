from sqlite3 import connect
import requests
from bs4 import BeautifulSoup

url = "http://kun.uz/news/main"
try:
    r = requests.get(url)
    print("Success!")
except Exception as error:
    print(f"Error during connecting to {url}")

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_= 'news-title')
print(news[0].text)
