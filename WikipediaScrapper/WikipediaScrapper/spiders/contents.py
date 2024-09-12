import sys

import scrapy


def debug(*msg, separator=True):
    print(msg)
    if separator:
        print('_' * 40)


class WikipediaScrapperContentsSpider(scrapy.Spider):
    name = 'WikipediaContents'

    def start_requests(self):
        url = 'https://en.wikipedia.org/wiki/Wikipedia:Contents'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        for li in response.css('#mw-content-text > div.mw-content-ltr.mw-parser-output > div:nth-child(4) > ul > li'):
            yield li.css('a::attr(href)').get()
        for li in response.css('#mw-content-text > div.mw-content-ltr.mw-parser-output > div:nth-child(6) > ul > li'):
            yield li.css('a::attr(href)').get()
