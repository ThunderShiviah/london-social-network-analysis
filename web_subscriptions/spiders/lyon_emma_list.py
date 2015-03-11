# -*- coding: utf-8 -*-
import scrapy

from web_subscriptions.items import ListItem

class LyonEmmaListSpider(scrapy.Spider):
    name = "lyon_emma_list"
    allowed_domains = ["http://digital.lib.ucdavis.edu/projects/bwrp/Works/LyonEMisce.htm"]
    start_urls = (
        'http://digital.lib.ucdavis.edu/projects/bwrp/Works/LyonEMisce.htm',
    )

    def parse(self, response):
        for sel in response.xpath('//body'):
            item = ListItem()
            item['name'] = sel.xpath('//ul/li/text()').extract()
            item['location'] = sel.xpath('//strong/em/text()').extract()
            yield item
