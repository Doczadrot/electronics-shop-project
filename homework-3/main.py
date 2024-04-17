from src.item import Item

if __name__ == '__main__':
    # Создаем экземпляр объекта Item
    item1 = Item("Смартфон", 10000, 20)

    # Проверяем его представление с помощью утверждений
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
