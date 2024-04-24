# keyboard.py
from src.item import Item
from .language_mixin import LanguageMixin


class Keyboard(eval(Item.get_class_string()), LanguageMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @staticmethod
    def get_class_string():
        return "Keyboard"