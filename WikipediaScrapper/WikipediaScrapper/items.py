# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikipediascrapperItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()


class PageItem(scrapy.Item):
    title = scrapy.Field()
    headings = scrapy.Field()
    paragraphs = scrapy.Field()
    links = scrapy.Field()
    images = scrapy.Field()
