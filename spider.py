from urllib.request import urlopen
from ingredients_finder import IngredientFinder
from general import *


class Spider:

    def __init__(self, url):
        self.page_url = url


    @staticmethod
    def gather_ingredients(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = IngredientFinder()
            finder.feed(html_string)
        except:
            print("Can't crawl page")
            return dict()
        return finder.recipe_ingredients()
