from general import *
import re
from fractions import Fraction


basket = load_previous_cart()

with open('recipes.txt', 'r') as input_file:
    lines = input_file.read().splitlines()

for i in range(0, len(lines)):
    lines[i] = 'https://jamilacuisine.ro/' + re.sub("\\s+", "-", lines[i]) + '-reteta-video/'
    current_cart = gather_ingredients(lines[i])
    for i in current_cart.keys():
        if i not in basket:
            basket[i] = current_cart[i]
        else:
            if basket[i]['unit'] is None:
                basket[i]['amount'] = basket[i]['amount'] + ' + ' + (current_cart[i]['amount'])
            if basket[i]['unit'] == current_cart[i]['unit'] and basket[i]['unit']:
                if basket[i]['amount'] is not int:
                    basket[i]['amount'] = float(Fraction(basket[i]['amount'])) + float(
                        Fraction(current_cart[i]['amount']))
                else:
                    basket[i]['amount'] = int(basket[i]['amount']) + int(current_cart[i]['amount'])
            else:
                pass


write_to_json(basket)
