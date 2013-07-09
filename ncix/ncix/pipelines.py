import sqlite3
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class NcixPipeline(object):
    def process_item(self, item, spider):
        return item

class NcixItemDupPipeline(object):
    from scrapy.exceptions import DropItem
    def __init__(self):
        self.sku_seen = set()
    
    def process_item(self, item, spider):
        if item['sku'] in self.sku_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.sku_seen.add(item['sku'])
            return item


class NcixStoreItemPipeline(object):
    from scrapy.exceptions import DropItem
    def __init__(self):
        self.database = sqlite3.connect('/home/yao/ncix_spider/prices.db')
        self.dbc = self.database.cursor()
    
    def process_item(self, item, spider):
        db_item=(item['product'], 
                 item['sku'], 
                 str(item['url']), 
                 str(item['part_number']), 
                 int(item['date']),
                 float(item['price']))
        self.dbc.execute("INSERT INTO NCIX VALUES (?,?,?,?,?,?)", db_item)
        self.database.commit()
        return item

    def __exit__(exit):
        self.database.close()
