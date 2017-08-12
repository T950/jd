# -*- coding: utf-8 -*-
import scrapy,re,time
from selenium import webdriver
from lxml import etree
from bs4 import BeautifulSoup
from scrapy.http import Request
class GupSpider(scrapy.Spider):
    name = 'gup'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['http://finance.sina.com.cn/data/#stock']
    #
    def start_requests(self):
        for i in range(0,5):
            n=i+1
            start_urls = 'http://finance.sina.com.cn/data/#stock'
            yield Request(start_urls,callback=self.parse,meta={'page':str(n)},dont_filter=True)
    def parse(self, response):
        # print(response.text)
        # demo=BeautifulSoup(response.text,'lxml').find_all('td',class_=True)
        # for i in demo:
        #     print(i.get_text())
        demo=re.compile('<tr><td class="tableCellAlignLeft"><a.*?>(.*?)</a></td><td.*?><a.*?>(.*?)</a></td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?><a.*?><span.*?></span></a></td></tr>',re.S)
        lists=demo.findall(response.text)
        def trips(first):
            first = re.sub('<span class=".*?" style="color: rgb(.*?);">|</span>|<span class="undefined">.*?', '',first)
            return first
        for a, b, c, d, e, f, g, h, i, j, k, l, m in lists:
            i=map(trips,[a, b, c, d, e, f, g, h, i, j, k, l, m])
            i=list(i)
            print(i)

