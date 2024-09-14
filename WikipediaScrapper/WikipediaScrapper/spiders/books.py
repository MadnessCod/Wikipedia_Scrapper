import scrapy


class BooksSpider(scrapy.Spider):
    name = 'WikipediaBooks'

    def start_requests(self):
        url = 'https://en.wikibooks.org/wiki/Main_Page'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        pass
