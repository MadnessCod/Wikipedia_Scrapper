import scrapy
from WikipediaScrapper.items import WikipediascrapperItem


class WikipediaScrapper(scrapy.Spider):
    name = 'wikipedia'

    def start_requests(self):
        url = 'https://en.wikipedia.org/wiki/Main_Page'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        featured_article = response.css('#mp-tfa > p')
        feature_article_link = response.css('#mp-tfa > p > i:nth-child(1) > b > a::attr(href)').get()
        featured_article_title = response.css('#mp-tfa > p > i:nth-child(1) > b > a::attr(title)').get()
        featured_article_text = featured_article.css('::text').getall()

        for news in response.css('#mp-itn > ul > li'):
            text = news.css('::text').getall()
            links = news.css('a::attr(href)').getall()

    def page_parse(self, response):

        pass
