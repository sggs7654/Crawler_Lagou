import scrapy
from scrapy_splash import SplashRequest

class MainSpider(scrapy.Spider):
    name = 'main'
    
    def start_requests(self):
        local = "D:\\python project\\spider\\practice\\WebSpiderPractice\\test.txt"
        with open(local, 'r+') as f:
            cookies = eval(f.read())
        url = 'https://www.lagou.com/zhaopin/CTO/?filterOption=3'
        script = """
        function main(splash)
            splash:clear_cookies()
            splash:init_cookies(splash.args.cookies)
            assert(splash:go(splash.args.url))
            assert(splash:wait(splash.args.wait))
            return {cookies = splash:get_cookies(),html = splash:html(),k=1111}
        end
        """
        yield SplashRequest(url, self.parse, endpoint='execute', args={'lua_source':script,'wait':1}, cookies=cookies)

    def parse(self, response):
        total_page_num = int(response.xpath(".//span[@class='span totalNum']/text()").get())
        # 用列表解析生成urls
        # for url in urls: yeild ...
        from scrapy.shell import inspect_response
        inspect_response(response, self)
        pass