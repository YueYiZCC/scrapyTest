# -*- coding: utf-8 -*-
import scrapy
import sys
#from spider.lian_jia.lian_jia.items import LianJiaItem
from ..items  import LianJiaItem
class LianjiapriceSpider(scrapy.Spider):
    name = 'lianjiaprice'
    allowed_domains = ['lianjia.com/']
    url='https://gz.fang.lianjia.com/loupan/pg'
    url_2='https://gz.lianjia.com/ershoufang/pg' #二手
    url2 = 'https://gz.fang.lianjia.com/loupan/pg1'
    # start_urls = ['http://https://gz.lianjia.com//']
    offset = 1
    start_urls = [url_2 + str(offset)]


    #start_urls = [url,url2]




    def parse(self, response):
        print("\n--------------------------------------------------\n")
        print(response)
        print("\n--------------------------------------------------\n")
        # for each in response.xpath("//li[@class='has-results']"):
       #for each in response.xpath("//ul[@class='resblock-list-wrapper']/li[@class='resblock-list post_ulog_exposure_scroll has-results']"):
        for each in response.xpath(".//li[@class='resblock-list post_ulog_exposure_scroll has-results']"):


            # 初始化模型对象
            item = LianJiaItem()

            #print(each.xpath('//a/@title').extract())
            #print(each.xpath('.//a[@class="name dig-click-event"]/text()').extract()[0] )
            name=each.xpath(".//a[@class='name dig-click-event']/text()").extract_first()

            address = each.xpath(".//div[@class='resblock-location']/a/text()").extract_first()
            price = each.xpath(".//div[@class='main-price']/span[@class='number']/text()").extract_first()
            area = each.xpath(".//div[@class='resblock-area']/span/text()").extract_first()

            # print("---------------: " + name)
            # print("---------------: " + price)
            # print("---------------: " + address)
            # print("---------------: " + area+"\n")

            item['name']=name
            item['price'] = price
            item['address'] = address
            item['area'] = area
            yield item
            # print(each.xpath("//[@class='resblock-name']text()"))
            # print(each.xpath("---------------"))
            # pass
        if self.offset < 100:
            self.offset += 1
            # 每次处理完一页的数据之后，重新发送下一页页面请求,一共100页
            # self.offset自增1，同时拼接为新的url，并调用回调函数self.parse处理Response
            newurl=self.url_2 + str(self.offset)
            print(newurl)
        #dont_filter=True  添加，不然会报错  显示 Filtered offsite request to 错误.
        #  你要request的地址和allow_domain里面的冲突，从而被过滤掉。可以停用过滤功能
            yield scrapy.Request(newurl, callback=self.parse,dont_filter=True)
