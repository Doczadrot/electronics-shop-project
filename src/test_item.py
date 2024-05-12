import csv
import unittest
import os
from src.item import Item, InstantiateCSVError

class TestItem(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый CSV-файл
        with open('test_items.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'price', 'quantity'])
            writer.writerow(['Item1', '1000', '5'])
            writer.writerow(['Item2', '1200', '3'])

    def tearDown(self):
        # Удаляем тестовый CSV-файл после тестов
        os.remove('test_items.csv')

    def test_instantiate_from_csv_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            Item.instantiate_from_csv('nonexistent.csv')

    def test_instantiate_from_csv_file_corrupted(self):
        # Создаем поврежденный CSV-файл
        with open('corrupted_items.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'price', 'quantity'])
            writer.writerow(['Item1', '1000', '5'])
            writer.writerow(['Item2', '1200'])  # Поврежденная строка

        with self.assertRaises(InstantiateCSVError):
            Item.instantiate_from_csv('corrupted_items.csv')

        # Удаляем поврежденный файл после теста
        os.remove('corrupted_items.csv')

if __name__ == '__main__':
    unittest.main()