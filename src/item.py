import os
import csv

class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: str, quantity: str):
        assert float(price) >= 0, f"Цена {price} должна быть больше или равна 0"
        assert int(quantity) >= 0, f"Количество {quantity} должно быть больше или равно 0"

        self._full_name = name
        self.price = float(price)
        self.quantity = int(quantity)
        Item.all.append(self)

    @property
    def name(self):
        if len(self._full_name) > 10:
            return self._full_name[:10]
        else:
            return self._full_name

    @name.setter
    def name(self, value):
        self._full_name = value
        Item.all.remove(self)
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    def __repr__(self):
        return f"Item('{self._full_name}', {self.price:.1f}, {self.quantity})"

    def __str__(self):
        return self.name

    @classmethod
    def instantiate_from_csv(cls, csv_file_path):
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            items = [cls(row['name'], float(row['price']), int(row['quantity'])) for row in reader]
        return items

    @staticmethod
    def string_to_number(string):
        try:
            return float(string)
        except ValueError:
            return 0.0