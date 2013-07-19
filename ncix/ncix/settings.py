# Scrapy settings for ncix project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
LOG_LEVEL = 'INFO'
BOT_NAME = 'ncix'
DOWNLOAD_DELAY = 6
DEPTH_LIMIT = 2
SPIDER_MODULES = ['ncix.spiders']
NEWSPIDER_MODULE = 'ncix.spiders'
DUPEFILTER_CLASS = 'ncix.ncixdupefilter.NCIXDupeFilter'
LOG_FILE = 'output.log'
ROBOTSTXT_OBEY = True
AUTOTHROTTLE_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'ncix.middleware.rand_useragent.RandomUserAgentMiddleware':400,
}

ITEM_PIPELINES = [
    'ncix.pipelines.NcixItemDupPipeline',
    'ncix.pipelines.NcixStoreItemPipeline',
]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ncix (+http://www.yourdomain.com)'
