import unittest
from unittest.mock import patch
from src.item import Item
from src.keyboard import Keyboard
from src.language_mixin import LanguageMixin

class TestKeyboard(unittest.TestCase):
    def setUp(self):
        self.keyboard = Keyboard('Dark Project KD87A', 9600, 5)

    def test_init(self):
        self.assertEqual(str(self.keyboard), 'Dark Project KD87A')
        self.assertEqual(str(self.keyboard.language), 'EN')

    def test_change_lang(self):
        self.keyboard.change_lang()
        self.assertEqual(str(self.keyboard.language), 'RU')
        self.keyboard.change_lang()
        self.assertEqual(str(self.keyboard.language), 'EN')

    def test_language_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.keyboard.language = 'CH'

    @patch('src.item.Item.get_class_string')
    def test_get_class_string(self, mock_get_class_string):
        mock_get_class_string.return_value = 'Item'
        self.assertEqual(Keyboard.get_class_string(), 'Keyboard')

    def test_inheritance(self):
        self.assertTrue(issubclass(Keyboard, Item))
        self.assertTrue(issubclass(Keyboard, LanguageMixin))

if __name__ == '__main__':
    unittest.main()