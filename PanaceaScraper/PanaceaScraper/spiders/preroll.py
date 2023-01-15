import scrapy
from ..items import PreRollItem, PreRollItemLoader
import datetime


class PreRollSpider(scrapy.Spider):
    timestamp = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    name = 'pre-roll'
    start_urls = [
        'https://panaceawellness.com/_next/data/i1quyIsLVg0Eq9xMEfoUD/dispensary/middleborough-ma/medical/category/pre-rolls.json']

    def parse(self, response):
        """
        @url https://panaceawellness.com/_next/data/i1quyIsLVg0Eq9xMEfoUD/dispensary/middleborough-ma/recreational/category/flower.json
        @returns items 1 80
        @returns requests 0 0
        @scrapes name price cbd_potency tch_potency strain brand effect quantity
        """
        products = response.json()['pageProps']['products']

        for item in products:
            pre_roll = PreRollItemLoader(item=PreRollItem(), selector=item)
            pre_roll.add_value('timestamp', PreRollSpider.timestamp)
            pre_roll.add_value('name', item['name'])
            pre_roll.add_value('price', item['variants'][0]['priceRec']) 
            if not item['potencyCbd']['formatted']:
                cbd_potency = 'None'
            else:
                cbd_potency = item['potencyCbd']['range']
            pre_roll.add_value('cbd_potency', cbd_potency)
            pre_roll.add_value('tch_potency', item['potencyThc']['range'])
            pre_roll.add_value('strain', item['strainType'])
            pre_roll.add_value('brand', item['brand']['name'])
            if not item['effects']:
                effect = 'None'
            else:
                effect = item['effects']
            pre_roll.add_value('effect', effect)
            pre_roll.add_value('quantity', item['variants'][0]['quantity'])
            yield pre_roll.load_item()
