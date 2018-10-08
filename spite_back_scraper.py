import scrapy

import scrapy

'''
    Basic scrapy thing to just download the src urls
'''
class SpriteDownloader(scrapy.Spider):
    name = 'pokemon_sprite_thingy'
    start_urls = ['http://pkmn.net/?action=content&page=viewpage&id=8561']
    
    def parse(self, response):
        for poke in response.css('table tr td img'):
            yield {
                'img_src' : poke.xpath('@src').extract()[0]
            }