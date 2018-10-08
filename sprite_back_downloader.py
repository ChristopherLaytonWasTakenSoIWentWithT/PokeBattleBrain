import urllib.request
import json
'''
    Downloads sprites from the bulbapedia
        - sorry for the user-agent spoof bulbapedia!
'''
class PokemonDownloader():
    def __init__(self, urls):
        self.base_protocol = "http:"
        self.output = "sprites/"
        self.urls = urls
        self.img_type = 'png'
        self.base_url = '//pkmn.net'

    def start_download(self):
        i = 0
        for sprite_obj in self.urls:
            i = i + 1
            print('Downloading... ' + str(i) + ' of ' + str(len(self.urls)))
            download_url = self.base_protocol + self.base_url +  sprite_obj['img_src']
            print(download_url)
            req = urllib.request.Request(
                download_url, 
                data=None, 
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
            )
            contents = urllib.request.urlopen(req).read()
            img = open(self.output + download_url.split('/')[-1], 'w+b')
            img.write(contents)
            img.close()

json_file = open('outputs/back_output.json', 'r')
json_data = json_file.read()
downloader = PokemonDownloader(json.loads(json_data))
downloader.start_download()

