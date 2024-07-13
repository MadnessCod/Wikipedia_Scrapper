import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, url):
        self.url = url
        self.links = list()

    def request(self):
        try:
            self.response = requests.get(self.url)
        except requests.exceptions.RequestException as error:
            print(f'Requests Error: {error}')
        else:
            self.home_page()

    def home_page(self):
        soup = BeautifulSoup(self.response.text, 'html.parser')
        try:
            upper = soup.find('div', id='mp-upper')
            middle = soup.find('div', id='mp-lower')
            lower = soup.find('div', id='mp-bottom')
        except AttributeError as error:
            print(f'AttributeError: {error}')
        else:
            for div in upper.find_all('div'):
                if div.id == 'mp-left':
                    featured_article = div.find('p')
                    for link in featured_article.find_all('a'):
                        self.links.append(self.url + link.get('href'))
                        text = featured_article.text
            for a in middle.find_all('a'):
                self.links.append(self.url + a.get('href'))
            return self.links

    def download(self):
        pass


if __name__ == '__main__':
    home_page = Scrapper('https://en.wikipedia.org/wiki/Main_Page')
    print(home_page.request())
