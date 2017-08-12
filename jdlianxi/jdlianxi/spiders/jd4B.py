# -*- coding: utf-8 -*-
import scrapy,json
import requests,re
from bs4 import BeautifulSoup
from scrapy import Request
from lxml import etree
import chardet


class Jd4bSpider(scrapy.Spider):
    name = 'jd4B'
    # allowed_domains = ['http://gou.jd.com/search?keyword=%E7%94%B5%E8%A7%86%E6%9C%BA']
    # start_urls = ['http://http://gou.jd.com/search?keyword=%E7%94%B5%E8%A7%86%E6%9C%BA/']

    def start_requests(self):
        # name=input('输入查询的内容：')
        # url='http://gou.jd.com/search?keyword='+name+'&page=2'
        url='http://gou.jd.com/search?keyword=%E7%94%B5%E8%A7%86&page=2'
        yield Request(url=url,callback=self.parse)

    def parse(self, response):
        # print(response.text)
        demo=BeautifulSoup(response.text,'lxml').find_all('script',type="text/javascript")[1].get_text()
        demo1=re.compile('"result":\[(.*?)]',re.S)
        list=re.search(demo1,demo).group(1)
        demo2=re.compile('"sku_id":"(.*?)"',re.S)
        list1=demo2.findall(list)
        for i in list1:
            url='http://item.jd.com/'+i+'.html'
            self.url=url
            pattern=re.compile('\d+',re.S)
            self.pattern_id=re.search(pattern,self.url).group()
            yield Request(url=url,method='GET',dont_filter=True,callback=self.content)

    def content(self,response):
        # print(response.text)
        pattern=re.compile('commentVersion:\'(\d+)\'',re.S)
        conment_version=re.search(pattern,response.text).group(1)
        # print(conment_version)
        url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv' \
                '{comment_version}&productId={product_id}&score=0&sortType=6&page=0&pageSize=10' \
                '&isShadowSku=0'. \
            format(comment_version=conment_version,product_id=self.pattern_id)
        yield Request(url=url,method='GET',callback=self.conts)

    def conts(self,response):
        pattern=re.compile('\((.*?)\);',re.S)
        items=re.search(pattern,response.text)
        if items !=None and items.group(1) !=None:
            data = json.loads(items.group(1))
            ym=data.get('productCommentSummary')
            comment_count=ym.get('commentCount')
            comment_version=response.meta.get('comment_version')
            # print(comment_version)
            for i in range(0,int(int(comment_count)/10)+1):
                url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv' \
                    '{comment_version}&productId={product_id}&score=0&sortType=6&page={page}&' \
                    'pageSize=10&isShadowSku=0'. \
                format(comment_version=comment_version, product_id=self.pattern_id,page=i)
                yield Request(url=url,headers={'Referer': 'https://item.jd.com/%s.html'% self.pattern_id},method='GET',callback=self.contss)

    def contss(self,response):
        # print(response.text)
        detect=chardet.detect(response.body)
        encoding=detect.get('encoding','')
        body=response.body.decode(encoding,'ignore')
        pattern=re.compile('\((.*?)\);',re.S)
        items=re.search(pattern,body)
        # print(list)
        if items !=None and items.group(1) !=None:
            data=json.loads(items.group(1))
            # ping=data.get('productCommentSummary')
            # print(ping)
            content=data.get('comments')
            comment={}
            url={}
            list=[]
            lists=[]
            dict={}
            for c in content:
                comment = {
                    'referenceName': c.get('referenceName'),
                }
                url={'url':self.url}
                dict={
                    'userLevelName': c.get('userLevelName'),
                    'nickname': c.get('nickname'),
                    'user_id':c.get('id'),
                    'conten':c.get('content'),
                    'creationTime':c.get('creationTime'),
                }
            lists.append(url)
            list.append(dict)
            url['key1']=list
            comment['key']=lists
            print(comment)
            '''还没有完'''