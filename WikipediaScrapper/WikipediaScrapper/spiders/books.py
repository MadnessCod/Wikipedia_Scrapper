import scrapy


class BooksSpider(scrapy.Spider):
    name = 'WikipediaBooks'

    def start_requests(self):
        url = 'https://en.wikibooks.org/wiki/Main_Page'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        featured = response.css('#mp-content > div')
        for div in featured:
            print(div.css('::text').extract())
            print(div.css('a::attr(href)').extract())

