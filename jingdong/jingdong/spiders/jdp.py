# -*- coding: utf-8 -*-
import scrapy


class JdpSpider(scrapy.Spider):
    name = 'jdp'
    # allowed_domains = ['http://gou.jd.com/search?keyword=%E6%89%8B%E6%9C%BA']
    # start_urls = ['http://http://gou.jd.com/search?keyword=%E6%89%8B%E6%9C%BA/&page=2']
    def start_requests(self):
        name=input('输入内容：')
        url='http://gou.jd.com/search?keyword='+name+'&page=2'

    def parse(self, response):
        pass
