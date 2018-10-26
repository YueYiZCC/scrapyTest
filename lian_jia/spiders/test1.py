import scrapy


class Test1Spider(scrapy.Spider):
    """
    功能：爬取腾讯社招信息
    """
    # 爬虫名
    name = "test1"
    # 爬虫作用范围
    allowed_domains = ["tencent.com"]

    url = "http://hr.tencent.com/position.php?&start="
    offset = 0
    # 起始url
    start_urls = [url + str(offset)]

    def parse(self, response):
        print('1---1-----1-----1-------1------1----1-----1\n')
        print(response)
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            print('-----------------------------------')
