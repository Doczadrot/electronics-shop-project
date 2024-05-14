import unittest
from src.item import Item, InstantiateCSVError

class TestItem(unittest.TestCase):

    def test_instantiate_from_csv_file_not_found(self):
        with self.assertRaises(FileNotFoundError) as context:
            Item.instantiate_from_csv('nonexistent_file.csv')
        self.assertEqual(str(context.exception), 'Отсутствует файл item.csv')

    def test_instantiate_from_csv_file_corrupted(self):
        with self.assertRaises(InstantiateCSVError) as context:
            Item.instantiate_from_csv('corrupted_items.csv')
        self.assertEqual(str(context.exception), 'Файл item.csv поврежден')

    def test_instantiate_from_csv_file_empty(self):
        Item.instantiate_from_csv('empty_items.csv')
        self.assertEqual(len(Item.all), 0)

    def test_instantiate_from_csv_file_with_invalid_data(self):
        with self.assertRaises(InstantiateCSVError) as context:
            Item.instantiate_from_csv('invalid_data_items.csv')
        self.assertEqual(str(context.exception), 'Файл item.csv поврежден')

    def test_instantiate_from_csv_valid_file(self):
        Item.instantiate_from_csv('items.csv')
        self.assertGreater(len(Item.all), 0) 