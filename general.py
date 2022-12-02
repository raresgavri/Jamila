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


def load_previous_cart():
    basket = dict()
    if os.path.exists('shopping_list.json'):
        with open("shopping_list.json", "r") as f:
            data = f.read()

        # decoding the JSON to dictionay
        basket = json.loads(data)
        print('Previous cart loaded')
    return basket


def write_to_json(dictionary):
    # encoding to JSON
    data = json.dumps(dictionary)
    print(data)
    # write to a file
    with open("shopping_list.json", "w") as f:
        f.write(data)
