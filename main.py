from general import *
import re
import json
from fractions import Fraction

basket = dict()


if os.path.exists('shopping_list.json'):
    with open("shopping_list.json", "r") as f:
        data = f.read()

    # decoding the JSON to dictionay
    basket = json.loads(data)
    print('Previous cart loaded')


with open('recipes.txt', 'r') as input_file:
    lines = input_file.read().splitlines()

for i in range(0, len(lines)):
    lines[i] = 'https://jamilacuisine.ro/' + re.sub("\\s+", "-", lines[i]) + '-reteta-video/'
    current_cart = gather_ingredients(lines[i])
    for i in current_cart.keys():
        if i not in basket:
            basket[i] = current_cart[i]
        else:
            if basket[i]['unit'] is None:  basket[i]['amount'] = basket[i]['amount'] + ' + ' + (current_cart[i]['amount'])
            if basket[i]['unit'] == current_cart[i]['unit'] and basket[i]['unit']:
                if basket[i]['amount'] is not int:
                    basket[i]['amount'] = float(Fraction(basket[i]['amount'])) + float(
                        Fraction(current_cart[i]['amount']))
                else:
                    basket[i]['amount'] = int(basket[i]['amount']) + int(current_cart[i]['amount'])
            else:
                pass


# encoding to JSON
data = json.dumps(basket)
print(data)
# write to a file
with open("shopping_list.json", "w") as f:
    f.write(data)
