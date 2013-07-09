from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.shell import inspect_response

from ncix.items import ncixItem

class NcixSpider(CrawlSpider):
    name = "ncix"
    allowed_domains = ["ncix.com"]
    
    rules = (
        Rule(SgmlLinkExtractor(allow=('sku=*',), deny=('mode=*',)), callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=('minorcatid=*',), deny=('mode=*')))
        )

    def __init__(self, *args, **kwargs):
        super(NcixSpider, self).__init__(*args, **kwargs)

        self.start_urls = [kwargs.get('start_url')]

        if self.start_urls ==[None]:
            self.start_urls = ["http://ncix.com/products/?minorcatid=1263"]
            #self.start_urls = ["http://ncix.com/products/?mode=productdir"]
    
    def parse_item(self, response):
        import re
        import time
        hxs = HtmlXPathSelector(response)
        item = ncixItem()
        item['url'] = response.url
        item['product'] = str(hxs.select('//title/text()').extract()[0])
        item['sku'] = int(hxs.select('//div[@align="left"]//span[@class="normal"]/text()').extract()[0])
        item['part_number'] = str(hxs.select('//div[@align="left"]//span[@class="normal"]//b//u/text()').extract()[0])
        prices = hxs.select('//div[@id="div_price"]//font[@size="4"]//b/text()').extract()
        prices = filter(lambda a: a!='\n', prices)[-1]
        item['price'] = float(re.sub("[^0-9|\.]","", prices))
        item['date'] = int(time.time())
        return item

