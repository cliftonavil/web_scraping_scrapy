# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()


class SatackoverflowItem(scrapy.Item):
    name = scrapy.Field()
    location = scrapy.Field()
    score = scrapy.Field()


class AmazonItem(scrapy.Item):
    title = scrapy.Field()
    delivery_on = scrapy.Field()
    price = scrapy.Field()
    image_link = scrapy.Field()
