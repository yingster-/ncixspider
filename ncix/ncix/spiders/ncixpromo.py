from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy import log
import urlparse



from ncix.items import ncixItem

class NcixpromoSpider(BaseSpider):
    name = 'ncixpromo'
    allowed_domains = ['www.ncix.com']


    def start_requests(self):
        import urllib


        file = urllib.urlopen('http://ajax.ncix.com/pna/redirect.php?jsoncallback=?')
        url = ""
        for i in file.readlines():
            url = url.join(i)
        file.close()
        url = url.split('\"')
        url = "".join(i for i in url if "promo" in i)
        url = url.replace("\\","")
        url = urlparse.urljoin("http://www.ncix.com", url)
        log.msg("Starting from: "+url, level=log.INFO)
        yield Request(url)
    
    def parse(self, response):
        import re
        import time
        hxs = HtmlXPathSelector(response)
        """
        for block in hxs.select('//table[@bgcolor="#F3F3F3"]//table[@align="center"]'):
            item = ncixItem()
            item['product'] = "".join(block.select('./tr/td[@class="normal" and @width="100%"]//text()').extract()).strip()
            item['url'] = "".join(block.select('./tr/td[@class="normal" and @width="100%"]/a/@href').extract()).strip()
            item['part_number']=""
            prices = "".join(block.select('./tr/td[@class="normal" and @valign="top"]//b/font[@size="2"]/text()').extract()).strip()
            item['price'] = float(re.sub("[^0-9|\.]","", prices))
            item['date'] = int(time.time())
            sku = "".join(block.select('./tr/td[@class="normal" and @valign="top"]/font[@size="1"]/text()').extract()).strip().split('Sku:')[-1].split(')')[0]
            item['sku'] = int(sku)
            yield item
            """

        for block in hxs.select('//table[@align="center"]/tbody/tr/td[@class="normal"]'):
            item = ncixItem()
            item['product'] = "".join(block.select('./div[@style="clear:both; text-align:center"]')[0].select('.//text()').extract()).strip()
            url = "".join(block.select('./div[@style="clear:both; text-align:center"]')[0].select('./a/@href').extract()).strip()
            item['url'] = urlparse.urljoin("http://www.ncix.com", url)
            item['part_number']=""
            prices = "".join(block.select('./tr/td[@class="normal" and @valign="top"]//b/font[@size="2"]/text()').extract()).strip()
            item['price'] = float(re.sub("[^0-9|\.]","", prices))
            item['date'] = int(time.time())
            sku = "".join(block.select('./tr/td[@class="normal" and @valign="top"]/font[@size="1"]/text()').extract()).strip().split('Sku:')[-1].split(')')[0]
            item['sku'] = int(sku)
            yield item
        


