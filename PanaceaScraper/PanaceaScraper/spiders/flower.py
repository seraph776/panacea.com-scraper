import scrapy
from ..items import FlowerItem, FlowerItemLoader
import datetime


class FlowerSpider(scrapy.Spider):
    timestamp = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    name = 'flower'
    start_urls = [
        'https://panaceawellness.com/_next/data/i1quyIsLVg0Eq9xMEfoUD/dispensary/middleborough-ma/recreational/category/flower.json']

    def parse(self, response):
        """
        @url https://panaceawellness.com/_next/data/i1quyIsLVg0Eq9xMEfoUD/dispensary/middleborough-ma/recreational/category/flower.json
        @returns items 1 80
        @returns requests 0 0
        @scrapes name price cbd_potency tch_potency strain brand effect quantity
        """
        products = response.json()['pageProps']['products']

        for item in products:
            flower = FlowerItemLoader(item=FlowerItem(), selector=item)
            flower.add_value('timestamp', FlowerSpider.timestamp)
            flower.add_value('name', item['name'])
            flower.add_value('price', item['variants'][0]['priceRec'])        
            if not item['potencyCbd']['formatted']:
                cbd_potency = 'None'
            else:
                cbd_potency = item['potencyCbd']['range']
            flower.add_value('cbd_potency', cbd_potency)
            flower.add_value('tch_potency', item['potencyThc']['range'])
            flower.add_value('strain', item['strainType'])
            flower.add_value('brand', item['brand']['name'])
            if not item['effects']:
                effect = 'None'
            else:
                effect = item['effects']
            flower.add_value('effect', effect)
            flower.add_value('quantity', item['variants'][0]['quantity'])
            yield flower.load_item()
