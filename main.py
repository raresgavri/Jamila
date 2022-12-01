from general import *
from spider import Spider


basket = dict()
shopping_list = prepare_data_files('shopping_list.json')

spider1 = Spider('https://jamilacuisine.ro/negresa-cu-dovleac-si-ciocolata-reteta-video/')
print(spider1.gather_ingredients('https://jamilacuisine.ro/negresa-cu-dovleac-si-ciocolata-reteta-video/'))

