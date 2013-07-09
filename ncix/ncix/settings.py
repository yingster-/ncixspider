# Scrapy settings for ncix project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
LOG_LEVEL = 'INFO'
BOT_NAME = 'ncixbot'
DOWNLOAD_DELAY = 4
DEPTH_LIMIT = 1
SPIDER_MODULES = ['ncix.spiders']
NEWSPIDER_MODULE = 'ncix.spiders'
DUPEFILTER_CLASS = 'ncix.ncixdupefilter.NCIXDupeFilter'
LOG_FILE = 'output.log'
ROBOTSTXT_OBEY = True
AUTOTHROTTLE_ENABLED = True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ncix (+http://www.yourdomain.com)'
