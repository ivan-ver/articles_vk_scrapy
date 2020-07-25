from scrapy import Spider
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from articles_vk_scrapy.items import ArticleVk




class SimpleSpiderSpider(Spider):
    name = 'simple_spider'
    start_urls = ['https://vk.com/@yvkurse/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = LinkExtractor('@yvkurse').extract_links(response)
        for url in urls:
            yield Request(url=url.url, callback=self.parse_article)

    def parse_article(self, response):
        art = ArticleVk()
        art['title'] = response.xpath("//h1/text()").get()
        art['text'] = " ".join(response.xpath("//p/descendant::text()").extract())
        art['ImageURL1'] = response.xpath("//img[@class]/@src").extract()[0]
        art['ImageURL2'] = response.xpath("//img[@class]/@src").extract()[1]
        yield art


