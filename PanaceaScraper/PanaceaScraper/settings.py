BOT_NAME = 'PanaceaScraper'

SPIDER_MODULES = ['PanaceaScraper.spiders']
NEWSPIDER_MODULE = 'PanaceaScraper.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'data/%(name)s/%(name)s_%(time)s.csv':{
        'format':'csv'
    }
}


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

FEED_EXPORT_FIELDS = [ 'timestamp', 'name', 'price', 'cbd_potency', 'tch_potency', 'strain', 'brand', 'effect', 'quantity']

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
