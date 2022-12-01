import os
import json


def prepare_data_files(cart_file):
    if not os.path.exists(cart_file):
        print('Creating shopping basket: ' + cart_file)
        with open(cart_file, 'w') as f:
            print("The json file is created")
            return f
    elif os.path.exists(cart_file):
        with open(cart_file) as user_file:
            basket = json.load(user_file)
            print('Basket loaded')
            return user_file
