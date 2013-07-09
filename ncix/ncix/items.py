# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ncixItem(Item):
    url = Field()
    product = Field()
    sku = Field()
    part_number = Field()
    price = Field()
    date = Field()
