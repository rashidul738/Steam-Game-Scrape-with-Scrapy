import scrapy
from ..items import StreamingItem

class StreamSpider(scrapy.Spider):
    name = 'stream'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers']

    def parse(self, response):
        stream_items = StreamingItem()
        games = response.xpath('//div[@id="search_resultsRows"]/a')
        for game in games:
            stream_items['game_url'] = game.xpath('.//@href').get()
            
