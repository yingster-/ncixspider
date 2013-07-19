from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from ncix.items import ncixItem

class NcixdailySpider(CrawlSpider):
    name = 'ncixdaily'
    allowed_domains = ['ncix.com']
    start_urls = ['http://www.ncix.com/']

    rules = (
        Rule(SgmlLinkExtractor(allow=('sku=*',), deny=('mode=*',)), callback='parse_item'),
        )

    def parse_item(self, response):
        import re
        import time
        hxs = HtmlXPathSelector(response)
        item = ncixItem()
        item['url'] = response.url
        item['product'] = hxs.select('//title/text()').extract()[0]
        item['sku'] = int(hxs.select('//div[@align="left"]//span[@class="normal"]/text()').extract()[0])
        item['part_number'] = hxs.select('//div[@align="left"]//span[@class="normal"]//b//u/text()').extract()[0]
        prices = hxs.select('//div[@id="div_price"]//font[@size="4"]//b/text()').extract()
        prices = filter(lambda a: a!='\n', prices)[-1]
        item['price'] = float(re.sub("[^0-9|\.]","", prices))
        item['date'] = int(time.time())
        return item

