from typing import Iterable, Any

import scrapy
from scrapy.http import Response


class WikipediaScrapper(scrapy.Spider):
    name = 'wikipedia'

    def start_requests(self) -> Iterable[scrapy.Request]:
        url = 'https://en.wikipedia.org/wiki/Main_Page'
        yield scrapy.Request(url,
                             meta={
                                 'playwright': True,

                             })

    def parse(self, response: Response, **kwargs: Any):
        yield response
