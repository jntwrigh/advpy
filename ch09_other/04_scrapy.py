"""
        04_scrapy.py

        Uses the 3rd Party tool: scrapy.  To use this module:
            1. pip install scrapy
            2. Open a terminal window, browser to the folder where this file resides, type:

                      scrapy runspider 04_scrapy.py -s LOG_ENABLED=False

"""
import scrapy


class YahooCrawler(scrapy.Spider):
    name = "yCrawler"

    def start_requests(self):
        urls = [
            'https://www.yahoo.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.css('.js-stream-item-title::text')[0].extract())

