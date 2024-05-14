# src/item.py
import csv
import os


class InstantiateCSVError(Exception):
    """Исключение, возникающее при повреждении файла CSV."""
    pass


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        assert price >= 0, f"Цена {price} должна быть больше или равна 0"
        assert quantity >= 0, f"Количество {quantity} должно быть больше или равно 0"

        self._full_name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def display_info(self):
        print(f"{self._full_name}: {self.price} ({self.quantity} шт.)")

    @classmethod
    def instantiate_from_csv(cls, path='items.csv'):
        cls.all = []
        full_path = os.path.join(os.path.dirname(__file__), path)
        if not os.path.exists(full_path):
            raise FileNotFoundError('Отсутствует файл item.csv')

        try:
            with open(full_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                if reader:  # Проверяем, что файл не пустой
                    for row in reader:
                        # Проверяем, что ключ 'quantity' есть в словаре 'row'
                        if 'quantity' in row:
                            cls(row['name'], float(row['price']), int(row['quantity']))
        except (KeyError, ValueError, TypeError) as e:  # Добавили TypeError
            raise InstantiateCSVError('Файл item.csv поврежден') from e