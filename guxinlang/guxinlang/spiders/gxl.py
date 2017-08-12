# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from guxinlang.items import GuxinlangItem

import json
class GxlSpider(scrapy.Spider):
    name = 'gxl'
    allowed_domains = ['http://vip.stock.finance.sina.com.cn/mkt/#qbgg_hk']
    start_urls = ['http://vip.stock.finance.sina.com.cn/mkt/#qbgg_hk']

    def parse(self, response):
        # print(response.text)
        demo=BeautifulSoup(response.text,'lxml').find('div',id="tbl_wrap").find_all('tr')[1,-1]
        for i in demo:
            item=GuxinlangItem()
            lists=['a','b','c','d','e','f','g','h','i','j','k','l','m']
            for index,key in enumerate(lists):
                item[key]=i.find_all('td')[index].get_text()
            yield item





            # item = GuxinlangItem()
            # item['gxl']=json.dumps(i.get_text(),ensure_ascii=True)
            # yield item

