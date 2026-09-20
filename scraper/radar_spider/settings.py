BOT_NAME = 'radar_spider'
SPIDER_MODULES = ['radar_spider.spiders']
NEWSPIDER_MODULE = 'radar_spider.spiders'
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS_PER_DOMAIN = 2
DOWNLOAD_DELAY = 1
FEEDS = {'data/catalogo.jsonl': {'format': 'jsonlines', 'overwrite': True}}
