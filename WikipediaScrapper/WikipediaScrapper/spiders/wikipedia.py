import scrapy
from WikipediaScrapper.items import WikipediascrapperItem


def debug(*msg, separator=True):
    if separator:
        print('_' * 40)
    print(msg)
    if separator:
        print('_' * 40)


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
            news_items = WikipediascrapperItem()
            news_items['name'] = news.css('::text').get()
            news_items['link'] = news.css('a::attr(href)').get()

        ongoing_link = response.css('#mp-itn > div:nth-child(4) > div:nth-child(1) > b > a::attr(href)').get()
        for ongoing in response.css('#mp-itn > div:nth-child(4) > div:nth-child(1) > div > ul > li'):
            ongoing_items = WikipediascrapperItem()
            ongoing_items['name'] = ongoing.css('::text').get()
            ongoing_items['link'] = ongoing.css('a::attr(href)').get()

        recent_deaths_link = response.css('#mp-itn > div:nth-child(4) > div:nth-child(2) > b > a::attr(href)').get()
        for death in response.css('#mp-itn > div:nth-child(4) > div:nth-child(2) > div > ul > li'):
            death_items = WikipediascrapperItem()
            death_items['name'] = death.css('::text').get()
            death_items['link'] = death.css('a::attr(href)').get()

        for know in response.css('#mp-dyk > ul > li'):
            know_items = WikipediascrapperItem()
            know_items['name'] = know.css('::text').get()
            know['link'] = know.css('a::attr(href)').get()

        for event in response.css('#mp-otd > ul > li'):
            event_items = WikipediascrapperItem()
            event_items['name'] = event.css('::text').get()
            event_items['link'] = event.css('a::attr(href)').get()

        for more_event in response.css('#mp-otd > div:nth-child(5) > ul > li'):
            more_event_items = WikipediascrapperItem()
            more_event_items['name'] = more_event.css('::text').get()
            more_event_items['link'] = more_event.css('a::attr(href)').get()

        for element in response.css('#mp-tfp > table > tbody > tr > td:nth-child(2) > p:nth-child(1)'):
            element_items = WikipediascrapperItem()
            element_items['name'] = element.css('::text').get()
            element_items['link'] = element.css('a::attr(href)').get()

        for credit in response.css('#mp-tfp > table > tbody > tr > td:nth-child(2) > p:nth-child(2) > small'):
            credit_items = WikipediascrapperItem()
            credit_items['name'] = credit.css('::text').get()
            credit_items['link'] = credit.css('a::attr(href)').get()

        for recently_featured in response.css(
                '#mp-tfp > table > tbody > tr > td:nth-child(2) > div.potd-recent > div > ul > li'):
            recently_featured_items = WikipediascrapperItem()
            recently_featured_items['name'] = recently_featured.css('::text').get()
            recently_featured_items['link'] = recently_featured.css('a::attr(href)').get()

    def page_parse(self, response):
        header = response.css('#content > header').get()
        content = response.css('#mw-content-text > div.mw-content-ltr.mw-parser-output')
