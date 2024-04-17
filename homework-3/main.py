from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    print(repr(item1))  # Добавляем эту строку для вывода результата repr(item1)
    assert repr(item1) == f"Item('Смартфон', {10000:.1f}, {20})"
    assert str(item1) == 'Смартфон'
