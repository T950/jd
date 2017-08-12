# -*- coding: utf-8 -*-
import scrapy,re
from scrapy.http import Request
from lxml import etree

class LianjSpider(scrapy.Spider):
    name = 'lianj'
    allowed_domains = ["lianjia.com"]
    bush_urls = 'https://bj.lianjia.com/ershoufang/'
    def start_requests(self):
        # header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
        url=self.bush_urls
        yield Request(url,self.parse)
    def parse(self, response):
        for a in range(1,11):
            list1=etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li/a/img/@src')
            list2=etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li/div/div/a/text()')
            list3=etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[2]/div/text()')
            list4=etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[3]/div/text()')
            list5 = etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div/text()')
            list7 = etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[6]/div[1]/text()')
            list6=etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[6]/div/span/text()')
                # print(list)
            for i in range(1,len(list1)+1):
                list1 = etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li['+str(i)+']/a/img/@src')
                list2 = etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li['+str(i)+']/div/div/a/text()')
                list3 = etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li['+str(i)+']/div[1]/div[2]/div/text()')
                list4 = etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li['+str(i)+']/div[1]/div[3]/div/text()')
                list5 = etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li['+str(i)+']/div[1]/div/text()')
                list7 = etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li['+str(i)+']/div[1]/div[6]/div[1]/text()')
                list6 = etree.HTML(response.text).xpath('/html/body/div[4]/div[1]/ul/li['+str(i)+']/div[1]/div[6]/div/span/text()')
                print(list1[0], list2[0], list3[0], list4[0], list5[0], list6[0], list7[0])
                # if list1 and list2 and list3 and list4 and list5 and list6 and list7:
                #     print(list1[0], list2[0], list3[0], list4[0], list5[0],list6[0],list7[0])