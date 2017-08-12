# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
from gupiao.agentes import agents
from gupiao.prox import proxy
import random,time
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
class Javasriptmiddle(object):


    def process_request(self,request,spider):
        dr=webdriver.PhantomJS()
        dr.get(request.url)
        time.sleep(3)
        body = dr.page_source
        page = request.meta['page']
        dr.find_element_by_xpath('//*[@id="pageDiv_0"]/input[1]').clear()
        dr.find_element_by_xpath('//*[@id="pageDiv_0"]/input[1]').send_keys(page)
        dr.find_element_by_xpath('//*[@id="pageDiv_0"]/input[2]').click()

        time.sleep(3)
        body = dr.page_source
        dr.get_screenshot_as_file('1.jpg')
        return HtmlResponse(dr.current_url,body=body.replace(u'\xa9',u''),encoding='utf-8',request=request)


# class AgentMiddleware(UserAgentMiddleware):
#     def process_request(self, request, spider):
#         agent=random.choice(agents)
#         request.headers['User-Agent']=agent

# class IpMiddleware(object):
#     def process_request(self,request,spider):
#         proxs=random.choice(proxy)
#         request.headers['proxy']=proxs




class GupiaoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
