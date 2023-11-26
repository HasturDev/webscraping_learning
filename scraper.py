import scrapy
from urllib.parse import urlparse

class DomainSpider(scrapy.Spider):
    name = 'domain_spider'
    allowed_domains = ['example.com']  # Change to your target domain
    start_urls = ['http://example.com']  # Change to your starting URL

    def parse(self, response):
        # Process the response using either response.xpath or response.css
        # For example:
        for href in response.css('a::attr(href)').extract():
            yield response.follow(href, self.parse)

        # You can also extract data and yield Scrapy Items
