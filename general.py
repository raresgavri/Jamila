import os
import json
from urllib.request import urlopen
from ingredients_finder import IngredientFinder





def gather_ingredients(page_url):
    html_string = ''
    try:
        print("Now crawling " + page_url)
        response = urlopen(page_url)
        if response.getheader('Content-Type') == 'text/html; charset=UTF-8':
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
        finder = IngredientFinder()
        finder.feed(html_string)
    except:
        print("Can't crawl page")
        return dict()
    return finder.recipe_ingredients()
