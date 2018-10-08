import scrapy

'''
    Basic scrapy thing to just download the src urls
'''
class SpriteDownloader(scrapy.Spider):
    name = 'pokemon_sprite_thingy'
    start_urls = ['http://pokedream.com/pokedex/pokemon?display=gen1']
    def getClass(self,element):
        return element.xpath('@class').extract()
    def parse(self, response):
        for poke in response.css('table tr'):
            pokemon = {}
            name_element = poke.css('td:first-child')
            name = self.getClass(name_element)
            if len(name)> 0:
                pokemon['name'] = name[0]
            else:
                continue
            index_element = poke.css('td:nth-child(2)')
            index = index_element.xpath('text()').extract_first()
            pokemon['id'] = int(index)
            type_element = poke.css('td:nth-child(4)')
            type_1 = self.getClass(type_element)
            if len(type_1) > 0:
                pokemon['type1'] = type_1[0]
            else:
                continue
            yield pokemon