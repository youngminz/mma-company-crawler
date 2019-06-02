BOT_NAME = 'mma'
LOG_FORMAT = "[%(levelname)-5s %(asctime)s %(name)s:%(lineno)s %(funcName)s] %(message)s"
SPIDER_MODULES = ['mma.spiders']
NEWSPIDER_MODULE = 'mma.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 1024
CONCURRENT_REQUESTS_PER_DOMAIN = 1024
CONCURRENT_REQUESTS_PER_IP = 1024
ITEM_PIPELINES = {
   'mma.pipelines.NormalizeString': 300,
   'mma.pipelines.SaveToMySQL': 900,
}
FEED_EXPORT_ENCODING = 'utf-8'
DOWNLOAD_FAIL_ON_DATALOSS = True
