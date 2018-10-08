import scrapy

'''
    Basic scrapy thing to just download the src urls
'''
class SpriteDownloader(scrapy.Spider):
    name = 'pokemon_sprite_thingy'
    start_urls = ['https://archives.bulbagarden.net/wiki/Category:Red_and_Blue_sprites']
    
    def parse(self, response):
        for poke in response.css('.thumb div a img'):
            yield {
                'img_src' : poke.xpath('@src').extract()[0]
            }