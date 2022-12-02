from html.parser import HTMLParser
from urllib import parse


class IngredientFinder(HTMLParser):

    def __init__(self):
        super().__init__()
        self.inside = False
        self.amount_tag = False
        self.unit_tag = False
        self.name_tag = False
        self.amount_value = 0
        self.unit_value = 0
        self.recipe = {}

    def handle_starttag(self, tag, attrs):

        if tag == 'span':
            for (attribute, value) in attrs:
                if attribute == 'class' and value == 'wprm-recipe-ingredient':
                    self.inside = True
                if attribute == 'class' and value == 'wprm-recipe-ingredient-amount':
                    self.amount_tag = True
                elif attribute == 'class' and value == 'wprm-recipe-ingredient-unit':
                    self.unit_tag = True
                elif attribute == 'class' and value == 'wprm-recipe-ingredient-name':
                    self.name_tag = True

    def handle_data(self, data):
        if self.amount_tag is True:
            self.amount_tag = False
            self.amount_value = data
        elif self.unit_tag is True:
            self.unit_tag = False
            self.unit_value = data
        if self.name_tag is True:
            self.recipe[data] = {'amount': self.amount_value, 'unit': self.unit_value}
            self.amount_value = self.unit_value = None
            self.name_tag = False

    def recipe_ingredients(self):
        return self.recipe

    def error(self, message):
        pass

