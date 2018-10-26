# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  json
from scrapy.conf import settings

class LianJiaPipeline(object):

    def __init__(self):
        print("\n\n--1--1---t1t-----t1t------1t-----t1t-------------1--1---\n\n")
        self.filename = open(r"C:\Users\zcc\Desktop\test_2.csv", "wb")
    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        print(text)
        print(text)
        self.filename.write(text.encode("utf-8"))
        return item
    def close_spider(self, spider):
        self.filename.close()
