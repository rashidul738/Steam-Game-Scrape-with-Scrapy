# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class StreamingItem(scrapy.Item):
    url = scrapy.Field(),
    img_url = scrapy.Field(),
    game_name = scrapy.Field(),
    release_date = scrapy.Field(),
    orginal_price = scrapy.Field(),
    dprice = scrapy.Field(),
    discount_rate = scrapy.Field()
