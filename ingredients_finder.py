from html.parser import HTMLParser
from urllib import parse

class IngredientFinder(HTMLParser):

    def __init__(self):
        super().__init__()
        self.amount=0
        self.unit=0
        self.name=0


    def handle_starttag(self, tag, attrs):

        if tag == 'span':
            for (attribute, value) in attrs:
                if attribute == 'class' and value == 'wprm-recipe-ingredient-amount':
                    self.amount=1
                elif attribute == 'class' and value == 'wprm-recipe-ingredient-unit':
                    self.unit=1
                elif attribute == 'class' and value == 'wprm-recipe-ingredient-name':
                    self.name=1

    def handle_data(self, data):
        if self.amount == 1:
            print('Encountered amount: ' + data)
            self.amount = 0
        elif self.unit == 1:
            print('Encountered unit: ' + data)
            self.unit = 0
        if self.name == 1:
            print('Encountered name: ' + data)
            self.name = 0




    def error(self, message):
        pass


parser = IngredientFinder()
parser.feed('<li class="wprm-recipe-ingredient" style="list-style-type: none;" data-uid="0">'
            '<span class="wprm-recipe-ingredient-amount">400</span> '
            '<span class="wprm-recipe-ingredient-unit">g</span> '
            '<span class="wprm-recipe-ingredient-name">faina</span></li>'
            '<li class="wprm-recipe-ingredient" style="list-style-type: none;" data-uid="6">'
            '<span class="wprm-checkbox-container"><input type="checkbox" id="wprm-checkbox-5" class="wprm-checkbox" aria-label="&nbsp;putina  sare">'
            '<label for="wprm-checkbox-5" class="wprm-checkbox-label">'
            '<span class="sr-only screen-reader-text wprm-screen-reader-text">▢ </span></label></span>'
            '<span class="wprm-recipe-ingredient-amount">putina </span> '
            '<span class="wprm-recipe-ingredient-name">sare</span></li>')