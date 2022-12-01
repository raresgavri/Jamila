from urllib.request import urlopen
from ingredients_finder import IngredientFinder
from general import *

class Spider:

    # Shared
    project_name = ''
    url = ''


    def __init__(self, project_name, url):
        self.boot()
        self.crawl_page()

    @staticmethod
    def crawl_page(thread_name, page_url):
        print(thread_name + ' now crawling ' + page_url)
