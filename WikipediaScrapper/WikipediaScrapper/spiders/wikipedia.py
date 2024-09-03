import scrapy

from WikipediaScrapper.items import WikipediascrapperItem


class WikipediaScrapper(scrapy.Spider):
    name = 'wikipedia'

    def start_requests(self):
        url = 'https://en.wikipedia.org/wiki/Main_Page'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        top_left = response.xpath('//*[@id="mp-left"]')
        top_right = response.xpath('//*[@id="mp-right"]')
        top_left_text = top_left.xpath('.//text()').extract()
        top_left_links = top_left.xpath('.//a/@href').getall()

        for link in top_left_links:
            try:
                yield response.follow(link, callback=self.page_parse)
            except ValueError:
                self.log(f'invalid link: {link}')


    def page_parse(self, response):
        page_item = WikipediascrapperItem()
        if '.jpg' in response.url:
            debug(f'found an image the url is {response.url}')
            yield {
                'image_urls': response.url
            }
