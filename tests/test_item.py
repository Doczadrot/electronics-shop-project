import os
import pytest
from src.item import Item

test_dir = os.path.dirname(os.path.abspath(__file__))
test_items_file = os.path.join(test_dir, 'test_items.csv')


@pytest.fixture(autouse=True)
def clear_item_all():
    # Очищаем список all перед каждым тестом
    Item.all.clear()
    yield  # Выполняем тест
    # Очищаем список all после каждого теста
    Item.all.clear()


@pytest.fixture
def item():
    # Создаем экземпляр класса Item для использования в тестах
    return Item("Test Item", 10.0, 5)


def test_instantiate_from_csv():
    # Создаем временный файл items.csv с данными для теста
    with open(test_items_file, 'w', encoding='utf-8') as file:
        file.write("name,price,quantity\n")
        file.write("Phone,100,1\n")
        file.write("Laptop,1000,3\n")
        file.write("Cable,10,5\n")

    # Инициализируем экземпляры класса Item из временного файла
    items = Item.instantiate_from_csv(test_items_file)

    # Проверяем, что все экземпляры добавлены в список all
    assert len(Item.all) == 3

    # Проверяем данные каждого экземпляра
    assert items[0].name == "Phone"
    assert items[0].price == 100.0
    assert items[0].quantity == 1

    assert items[1].name == "Laptop"
    assert items[1].price == 1000.0
    assert items[1].quantity == 3

    assert items[2].name == "Cable"
    assert items[2].price == 10.0
    assert items[2].quantity == 5


def test_string_to_number():
    # Проверяем преобразование строк в числа
    assert Item.string_to_number("10") == 10.0
    assert Item.string_to_number("5.5") == 5.5
    assert Item.string_to_number("abc") == 0.0


def test_name_getter_setter():
    # Создаем экземпляр класса Item
    item = Item("LongNameItem", 100, 1)

    # Проверяем геттер и сеттер для атрибута name
    assert item.name == "LongNameIt"  # Ожидается исходное имя

    item.name = "VeryLongName"
    assert item.name == "VeryLongNa"  # Ожидается обрезанное имя

    item.name = "Short"
    assert item.name == "Short"  # Ожидается исходное короткое имя без обрезки


def test_repr(item):
    assert repr(item) == "Item('Test Item', 10.0, 5)"


def test_str(item):
    assert str(item) == "Test Item"