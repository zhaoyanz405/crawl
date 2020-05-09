# -*- coding: utf-8 -*-
import scrapy


class CrawlSubjectSpider(scrapy.Spider):
    name = 'crawl_subject'
    allowed_domains = ['www.gjgwy.org/201911/437486.html']
    start_urls = ['http://www.gjgwy.org/201911/437486.html']

    def parse(self, response):
        filename = "teacher.html"
        open(filename, 'wb').write(response.body)
