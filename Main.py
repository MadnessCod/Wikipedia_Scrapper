import requests
from bs4 import BeautifulSoup

try:
    text = requests.get('https://en.wikipedia.org/wiki/', timeout=20)
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
else:
    soup = BeautifulSoup(text.text, 'html.parser')
    print(soup.find('h1'))
