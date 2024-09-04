import scrapy
from WikipediaScrapper.items import WikipediascrapperItem


class WikipediaScrapper(scrapy.Spider):
    name = 'wikipedia'

    def start_requests(self):
        url = 'https://en.wikipedia.org/wiki/Main_Page'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        featured_article = response.css('#mp-tfa > p')
        featured_article_img = response.css('#mp-tfa-img > div > span > a > img::attr(src)').get()
        feature_article_link = response.css('#mp-tfa > p > i:nth-child(1) > b > a::attr(href)').get()
        featured_article_title = response.css('#mp-tfa > p > i:nth-child(1) > b > a::attr(title)').get()
        featured_article_text = featured_article.css('::text').getall()

        for news in response.css('#mp-itn > ul > li'):
            text = news.css('::text').getall()
            links = news.css('a::attr(href)').getall()

        ongoing_link = response.css('#mp-itn > div:nth-child(4) > div:nth-child(1) > b > a::attr(href)').get()
        for ongoing in response.css('#mp-itn > div:nth-child(4) > div:nth-child(1) > div > ul > li'):
            text = ongoing.css('::text').getall()
            links = ongoing.css('a::attr(href)').getall()

        recent_deaths_link = response.css('#mp-itn > div:nth-child(4) > div:nth-child(2) > b > a::attr(href)').get()
        for death in response.css('#mp-itn > div:nth-child(4) > div:nth-child(2) > div > ul > li'):
            text = death.css('::text').getall()
            links = death.css('a::attr(href)').getall()

        for know in response.css('#mp-dyk > ul > li'):
            text = know.css('::text').getall()
            links = know.css('a::attr(href)').getall()

        for event in response.css('#mp-otd > ul > li'):
            text = event.css('::text').getall()
            links = event.css('a::attr(href)').getall()

        for more_event in response.css('#mp-otd > div:nth-child(5) > ul > li'):
            text = more_event.css('::text').getall()
            links = more_event.css('a::attr(href)').getall()

        for element in response.css('#mp-tfp > table > tbody > tr > td:nth-child(2) > p:nth-child(1)'):
            text = element.css('::text').getall()
            links = element.css('a::attr(href)').getall()

        for credit in response.css('#mp-tfp > table > tbody > tr > td:nth-child(2) > p:nth-child(2) > small'):
            text = credit.css('::text').getall()
            links = credit.css('a::attr(href)').getall()

        for recently_featured in response.css('#mp-tfp > table > tbody > tr > td:nth-child(2) > div.potd-recent > div '
                                              '> ul > li'):
            text = recently_featured.css('::text').getall()
            links = recently_featured.css('a::attr(href)').getall()

    def page_parse(self, response):
        pass
