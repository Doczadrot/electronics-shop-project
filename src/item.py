class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        # Проверка входных данных
        assert price >= 0, f"Цена {price} должна быть больше или равна 0"
        assert quantity >= 0, f"Количество {quantity} должно быть больше или равно 0"

        # Присвоение атрибутов
        self.name = name
        self.price = price
        self.quantity = quantity

        # Добавление экземпляра в список всех экземпляров
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"