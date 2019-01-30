# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['stackshare.io']
    start_urls = ['https://stackshare.io/python']

    link_extractor = LinkExtractor(restrict_xpaths=['//div[@class="similar-service-logos"]'])
    rules = (scrapy.spiders.Rule(
        link_extractor, 
        callback='parse_item', 
        follow=True),
    )

    def parse_item(self, response):
        d = {}
        d['url'] = response.url
        xp = '//span[@itemprop="alternativeHeadline"]/text()'
        d['description'] = response.xpath(xp).extract()[0]

        xp = '//div[@class="col-md-1 stack-logo"]/a/@data-hint'
        d['companies'] = response.xpath(xp).extract()


        xp = '//form/label/span/div/span/text()'
        xp1 = '//form/label/div/span/text()'
        votes = response.xpath(xp1).extract()
        reason = response.xpath(xp).extract()
        d['why'] = list(zip(votes, reason))
        yield d

