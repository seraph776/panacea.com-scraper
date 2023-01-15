from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import Item, ItemLoader
import scrapy


class FlowerItem(Item):
    timestamp = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    cbd_potency = scrapy.Field()
    tch_potency = scrapy.Field()
    strain = scrapy.Field()
    brand = scrapy.Field()
    effect = scrapy.Field()
    quantity = scrapy.Field()


class FlowerItemLoader(ItemLoader):
    name_in = MapCompose(str.strip)
    name_out = TakeFirst()
    price_out = TakeFirst()
    cbd_potency_out = TakeFirst()
    tch_potency_out = TakeFirst()
    quantity_out = TakeFirst()


class PreRollItem(Item):
    timestamp = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    cbd_potency = scrapy.Field()
    tch_potency = scrapy.Field()
    strain = scrapy.Field()
    brand = scrapy.Field()
    effect = scrapy.Field()
    quantity = scrapy.Field()


class PreRollItemLoader(ItemLoader):
    name_in = MapCompose(str.strip)
    name_out = TakeFirst()
    price_out = TakeFirst()
    cbd_potency_out = TakeFirst()
    tch_potency_out = TakeFirst()
    quantity_out = TakeFirst()

