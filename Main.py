import requests


try:
    text = requests.get('https://en.wikipedia.org/wiki/', timeout=20)
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')

