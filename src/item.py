import os
from src.language_mixin import LanguageMixin

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

    def change_price(self, multiplier: float):
        self.price *= multiplier

    @classmethod
    def instantiate_from_csv(cls, csv_file_path='items.csv'):
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"Отсутствует файл {csv_file_path}")

        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                required_fields = ['name', 'price', 'quantity']
                items = [cls(row['name'], float(row['price']), int(row['quantity'])) for row in reader]
                return items
        except (csv.Error, ValueError) as e:
            raise InstantiateCSVError("Файл item.csv поврежден") from e

if __name__ == '__main__':
    try:
        items = Item.instantiate_from_csv('data/items.csv')
        for item in items:
            item.display_info()
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    except InstantiateCSVError as e:
        print(f"Ошибка: {e}")